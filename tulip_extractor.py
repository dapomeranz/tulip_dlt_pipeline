import dlt
import requests
import json


@dlt.source
def tulip_table_source(
    api_secret_key=dlt.secrets.value,
    table_ids=dlt.secrets.value,
    table_names=dlt.secrets.value,
    instance_url=dlt.secrets.value,
):
    headers = {"Authorization": api_secret_key}

    def get_request_params(i, last_updated):
        return {
            "limit": 100,
            "offset": i * 100,
            "filters": json.dumps(
                [
                    {
                        "field": "_updatedAt",
                        "functionType": "greaterThan",
                        "arg": last_updated.start_value,
                    }
                ]
            ),
            "sortOptions": json.dumps([{"sortBy": "_updatedAt", "sortDir": "asc"}]),
        }

    def tulip_table_resource(
        table_id,
        headers,
        last_updated=dlt.sources.incremental("_updatedAt", "1970-01-01T00:00:00Z"),
    ):
        url = f"https://{instance_url}/api/v3/tables/{table_id}/records"
        i = 0
        while True:
            print(f"Fetching page {i} of {table_id}")
            print(f"Last updated: {last_updated.start_value}")
            results = requests.get(
                url, headers=headers, params=get_request_params(i, last_updated)
            )
            if results.status_code != 200 or len(results.json()) == 0:
                break
            i += 1
            yield results.json()

    for table_id, table_name in zip(table_ids, table_names):
        yield dlt.resource(
            tulip_table_resource,
            name=table_name,
            primary_key="id",
            write_disposition="replace",  # NOTE - switch to replace to do a full rebuild
        )(table_id, headers)


pipeline = dlt.pipeline(
    destination="postgres",  # NOTE - change this field depending on your destination e.g. switch to bigquery to use bigquery
    pipeline_name="tulip_table_pipeline",
    dataset_name="tulip_table_data",  # NOTE - dataset_name will be the name of the schema in your db
)

metadata = pipeline.run(tulip_table_source())
print(metadata)
