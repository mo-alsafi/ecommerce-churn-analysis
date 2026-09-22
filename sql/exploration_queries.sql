use `ecommerce-churn-data`;



SELECT * FROM ecommerce_churn LIMIT 50;

-- overall churn rate
SELECT 
    COUNT(*) AS total_customers,
    SUM(Churn) AS total_churned,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_pct
FROM ecommerce_churn;

-- churn rate by CityTier
SELECT 
    CityTier,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_pct
FROM ecommerce_churn
GROUP BY CityTier
ORDER BY CityTier;

--  avg tenure of churned vs. retained
SELECT 
    CASE 
        WHEN Churn = 1 THEN 'Churned'
        ELSE 'Retained'
    END AS customer_status,
    COUNT(*) AS customer_count,
    ROUND(AVG(Tenure), 2) AS avg_tenure_months
FROM ecommerce_churn
GROUP BY customer_status;

-- Churn rate for customers with complians vs not 
SELECT 
	CASE 
		WHEN Complain = 1 THEN "Complained"
		ELSE "Didn't Complain"
	END AS Compelain_Status,
    COUNT(*) as total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS Churn_rate
FROM ecommerce_churn
GROUP BY Compelain_Status;
    

SELECT COUNT(DISTINCT Complain) FROM ecommerce_churn;
