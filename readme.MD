## Tulip Data Extractor using dlt

dlt is an open source framework for extracting data from services such as REST APIs and converting them into normalized, relational tables inside of data warehouses. There are a ton of cool features which allow for very custom extraction pipelines to be developed, tested, and customized in many different ways.

### How To Use This Pipeline

1. Clone this git repository to a machine which has python 3.9+ installed.
2. Use pip to install the dlt library. Depending on which destination you are using you may need to install additional libraries. Reference [dlt for documentation on their destinations.](https://dlthub.com/docs/dlt-ecosystem/destinations/)
3. Configure the secrets.toml file using the example file as a template. Reference the [Tulip Knowledge Base](https://support.tulip.co/docs/how-to-use-the-table-api#:~:text=Navigate%20to%20the%20Settings%20page,top%20right%20of%20this%20page.) for necessary information on how to find your API keys and Table IDs.
4. Configure the secrets.toml file destination section to match the destination you are using. The example file is configured for a Postgres database. Reference [the dlt documentation](https://dlthub.com/docs/dlt-ecosystem/destinations/) for more information on how to configure other destinations.
5. Run the `tulip_extractor.py` file using python 3.9+.
