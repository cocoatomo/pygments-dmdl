.. Sample Doc for pygments-dmdl documentation master file, created by
   sphinx-quickstart on Thu Jun  2 13:30:43 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sample Doc for pygments-dmdl's documentation!
========================================================

Contents:

.. toctree::
   :maxdepth: 2

.. code-block:: dmdl

   a = {
       id : INT;
   };

   b = {
       name : TEXT;
   };

.. code-block:: dmdl

   // hoge

   /*
    * aaa
    */

   "desc"
   @attribute.a.b.c
   @attribute()
   @attribute(value = {"a", "b"})
   sample = {
       id : INT;
       name : TEXT;
       amount : INT;
   };

.. code-block:: dmdl

   projective partial = {
       a : BOOLEAN;
       b : DECIMAL;
       c : INT;
   };

.. code-block:: dmdl

   joined sample_extend = sample -> /* comment */ {
       id -> id;
       name -> name;
       amount -> amount;
   } % id + partial -> {
       a -> a;
       b -> b;
       c -> id;
   } % id;

.. code-block:: dmdl

   summarized sum_sample = sample => {
       any id -> id; // hogehoge
       sum int -> sum_int; -- fugafuga
   } % id;

.. code-block:: dmdl

   model_using_datetime = {
       dt : DATETIME;
       d : DATE;
   };

copied from https://github.com/asakusafw/asakusafw-examples/blob/master/example-basic-spark/src/main/dmdl/models.dmdl

.. code-block:: dmdl



   -- 入力CSVファイル形式

   "売上明細"
   @directio.csv(
       has_header = TRUE,
       datetime = "yyyy-MM-dd HH:mm:ss"
   )
   sales_detail = {

       "売上日時"
       @directio.csv.field(name = "日時")
       sales_date_time : DATETIME;

       "店舗コード"
       @directio.csv.field(name = "店舗コード")
       store_code : TEXT;

       "商品コード"
       @directio.csv.field(name = "商品コード")
       item_code : TEXT;

       "数量"
       @directio.csv.field(name = "数量")
       amount : INT;

       "販売単価"
       @directio.csv.field(name = "販売単価")
       unit_selling_price : INT;

       "販売金額"
       @directio.csv.field(name = "販売金額")
       selling_price : INT;

       "ファイル名"
       @directio.csv.file_name
       file_name : TEXT;
   };

   "店舗マスタ"
   @directio.csv(has_header = TRUE)
   store_info = {

       "店舗コード"
       @directio.csv.field(name = "店舗コード")
       store_code : TEXT;

       "店舗名称"
       @directio.csv.field(name = "名称")
       store_name : TEXT;
   };

   "商品マスタ"
   @directio.csv(
       has_header = TRUE,
       date = "yyyy-MM-dd"
   )
   item_info = {

       "商品コード"
       @directio.csv.field(name = "商品コード")
       item_code : TEXT;

       "商品名"
       @directio.csv.field(name = "商品名")
       item_name : TEXT;

       "商品部門コード"
       @directio.csv.field(name = "部門コード")
       department_code : TEXT;

       "商品部門名"
       @directio.csv.field(name = "部門名")
       department_name : TEXT;

       "商品カテゴリコード"
       @directio.csv.field(name = "カテゴリコード")
       category_code : TEXT;

       "商品カテゴリ名"
       @directio.csv.field(name = "カテゴリ名")
       category_name : TEXT;

       "商品単価"
       @directio.csv.field(name = "単価")
       unit_selling_price : INT;

       "マスタ登録日"
       @directio.csv.field(name = "登録日")
       registered_date : DATE;

       "マスタ適用開始日"
       @directio.csv.field(name = "適用開始日")
       begin_date : DATE;

       "マスタ適用終了日"
       @directio.csv.field(name = "適用終了日")
       end_date : DATE;
   };

   -- 中間データ形式

   "売上明細+商品マスタ"
   joined joined_sales_info
   = sales_detail -> {
       item_code -> item_code;
       amount -> amount;
       selling_price -> selling_price;
   } % item_code
   + item_info -> {
       item_code -> item_code;
       category_code -> category_code;
   } % item_code;


   -- 出力CSV形式

   "カテゴリ別売上集計"
   @directio.csv(
       has_header = TRUE
   )
   summarized category_summary = joined_sales_info => {

       @directio.csv.field(name = "カテゴリコード")
       any category_code -> category_code;

       @directio.csv.field(name = "販売数量")
       sum amount -> amount_total;

       @directio.csv.field(name = "売上合計")
       sum selling_price -> selling_price_total;
   } % category_code;

   "エラー情報"
   @directio.csv(
       has_header = TRUE
   )
   error_record = {

       "ファイル名"
       @directio.csv.field(name = "ファイル名")
       file_name : TEXT;

       "売上日時"
       @directio.csv.field(name = "日時")
       sales_date_time : DATETIME;

       "店舗コード"
       @directio.csv.field(name = "店舗コード")
       store_code : TEXT;

       "商品コード"
       @directio.csv.field(name = "商品コード")
       item_code : TEXT;

       "エラーメッセージ"
       @directio.csv.field(name = "メッセージ")
       message : TEXT;
   };

.. code-block:: dmdl

   ellipsis_sample = {
       ...

       "プロパティ"
       @attr
       property : DATETIME;

       ...
   };

   ellipsis_sample2 = {
       ...

       property2 : DATE;

       ...
   };

.. code-block:: dmdl

   abbreviated_property = {
       ...
   };

   joined abbreviated_mapping = hoge -> {
       ...
   } % aaa + fuga -> {
       ...
   } % aaa;

   summarized abbreviated_summarize = hoge => {
       ...
       ...
   } % aaa;

.. code-block:: dmdl

   <疑似要素> = {
       <プロパティ1> : <データタイプ1>;
       id : INT;
   };

.. code-block:: dmdl

   joined <結合モデル> = <モデル1> -> {
       "マッピング"
       <マップ元プロパティ> -> <マップ先プロパティ>;
   } % <マップ先プロパティ> + <モデル2> -> <マッピング定義> % <結合キー>;

.. code-block:: dmdl

   summarized <集計モデル> = <対象モデル> => {
       <集約関数> <集計元> -> <集計結果>;
   };

.. code-block:: dmdl

   projective <モデル名> = {
       <プロパティ> : <型>;
   };

.. code-block:: dmdl

   // trailing comma
   @attr(
      hoge = TRUE,
      fuga = "aaa",
   )
   mode = {
       ...
   };

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

