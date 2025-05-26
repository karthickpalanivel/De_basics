from pyspark.sql.functions import col, lit
customer_df = spark.sql("SELECT * FROM sixfive_db.customer")
customer_df.show()

policy_df = spark.sql("SELECT * FROM sixfive_db.policy")
policy_df.show()

payment_df = spark.sql("SELECT * FROM sixfive_db.payment")
payment_df.show()

# Filter customers over age 30
filtered_customers = customer_df.filter(col("Age") > 30)

# Add new column
policy_df = policy_df.withColumn("IsBonus", col("PolicyType") == "TermBonus")

# Rename column
payment_df = payment_df.selectExpr("Pid", "PName", "Years", "PaidAmt", "PType as PaymentMode")
payment_df.show()


# Join with broadcast
joined_df = filtered_customers.join(payment_df, ["Pid"], "inner")
joined_df.show()


# Repartition
repartitioned_df = joined_df.repartition(4)
repartitioned_df.show()


# ReduceByKey like transformation (simulated via groupBy)
agg_df = payment_df.groupBy("Pid").sum("PaidAmt")
agg_df.show()


# Cache
new_joined_df = joined_df.persist(StorageLevel.MEMORY_AND_DISK)
new_joined_df.show()

joined_df.write.mode("overwrite").format("parquet").saveAsTable("insurance_db.silver_insurance")


gold_df = joined_df.groupBy("Pid", "PolicyType").agg(
    {"PaidAmt": "sum"}
).withColumnRenamed("sum(PaidAmt)", "TotalPaid")

gold_df.write.mode("overwrite").saveAsTable("insurance_db.gold_policy_summary")
