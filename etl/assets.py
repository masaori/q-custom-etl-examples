"""ETL Assets for Dagster pipeline."""

from dagster import asset, AssetExecutionContext # type: ignore
from dagster_qai import QaiDagsterClient, CrawlConfig

@asset(
    kinds={"s3", "bronze", "python"},
)
def example_s3_bronze_asset(
    context: AssetExecutionContext,
    qai_client: QaiDagsterClient,
):
    """Example asset that reads from S3 and returns a list of dictionaries."""
    
    return qai_client.extract(
        context=context, 
        source_type="crawls",  
        config=CrawlConfig(
            user_id="hoge",
            config_base64="hoge"
        ),  
    )
