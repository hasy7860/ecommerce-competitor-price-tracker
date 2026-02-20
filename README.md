# Ecommerce Competitors Price Tracker

This project monitor product prices on a single Shopify store, stores historical data in PostgreSQL and sends instant email notifications when prices drop.

Its designed for ecommerce businesses who want to track competitor prices automatically without manual checking.

**Key Features:**
Scrapes a single shopify store product JSON endpoints
Stores historical variant-level pricing in PostgreSQL
Detects price drops between snapshots
Sends email alerts for new price drops
Fully configurable and reusable for any Shopify store

**Tech Stack**
Language: Python 3.x
Database: PostgreSQL
Libraries: requests, psycopg2, yagmail
Deployment: Local script (can be scheduled with cron)

**Architecture**
[Shopify JSON Endpoint]
           |
           v
    [Python Scraper] 
           |
           v
[PostgreSQL price_history table]
           |
           v
  [Price Drop Detection]
           |
           v
[Email Alerts via yagmail]

*I will continue from here tomorrow :(*
*I can't even use single bracket :)*

