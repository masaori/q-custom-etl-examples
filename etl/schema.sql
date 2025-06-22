CREATE TABLE IF NOT EXISTS irdb_hogehoge_ranking (
    -- テキストチャンクID
    id STRING,
    -- ユーザーID
    user_id STRING,
    -- ソースタイプ
    source_type STRING,
    -- ソースID
    source_id STRING,
    -- ソースグループID
    source_group_id STRING,
    -- ソースの作成時刻
    source_creation_time TIMESTAMP,
    -- チャンク化したテキスト
    text STRING,
    -- チャンクの全体のテキストにおける順番
    index INT,
    -- チャンク化したテキストが含まれていたファイルのURL
    url STRING,
    -- ファイル名
    title STRING,
    -- コンテンツタイプ
    content_type STRING
) PARTITIONED BY (
    source_type,
    source_group_id,
    user_id
) LOCATION 's3://ICEBERG_BUCKET_NAME/iceberg/ICEBERG_DB_NAME.db/text_chunks' TBLPROPERTIES (
    'table_type'='iceberg'
);