# Olist: Findings for Leadership
*Data: ~100k Olist marketplace orders, Jan 2017 – Aug 2018 · Full analysis in [`notebooks/`](notebooks/)*

## Summary
Olist grew fast in 2017 by winning new customers, but growth stalled in 2018, and almost none of those customers come back (2% return), so growth depends entirely on constantly acquiring new ones. Separately, late or failed deliveries, under 10% of orders, cause ~40% of all bad reviews, making delivery reliability the clearest lever for customer satisfaction.


**Recommendations**
1. **Fix delivery reliability:** set realistic promised dates and improve carrier performance in high-volume states.
2. **Invest in retention:** follow-up offers and re-engagement for first-time buyers.
3. **Protect top sellers:** dedicated support for the ~600 sellers who generate over 80% of revenue.

## 1. Is the business growing?
Strongly through 2017: revenue, orders and active customers rose several-fold. Growth came from **more customers**, not bigger baskets. In 2018 it **plateaued** at roughly 6,200–7,300 orders per month.

## 2. What drives revenue? (13.45M BRL total)
- **Categories:** the top 10 of 74 bring in 62%, a diversified portfolio.
- **Sellers:** highly concentrated. The top 20% bring in **82.5%**; the bottom half only ~3%. That's a dependency risk and a long-tail opportunity.

## 3. Do late deliveries hurt reviews?
Yes, strongly. Bad reviews (1–2 stars) rise from **9% when on time** to 32% at 1–3 days late and **79% at 8+ days**. Late orders are 7% of orders but cause about a third of bad reviews; orders that never arrive add more. The pattern holds in every major state, so it isn't a regional effect.

## 4. Do customers come back?
Rarely. Only **2.2%** of customers buy again, typically after ~2.5 months, and this hasn't improved over time.

## Caveats
- Correlation, not proof: the delivery–review link is strongly supported (it holds across states and gets worse with every extra day late), but it isn't tested by an experiment.
- Newer sellers and customers had less time in the data, which slightly understates their activity.
- Revenue = item prices excluding freight; canceled and unavailable orders are excluded.
- Open question: whether a bad delivery also lowers the chance of returning was not tested. Next step: compare return rates for customers whose first order was late vs. on time.