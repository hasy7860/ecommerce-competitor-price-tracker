import yagmail, os

def send_alert(drops):
    mail = yagmail.SMTP(user=os.getenv("originalhasy@gmail.com"),
                       password=os.getenv("ybrg tara ttbx iune"))
    
    body = "Price drop detected:\n\n"

    for variant_id, old_price, new_price in drops:
        body += f"Variant {variant_id}\n"
        body += f"Old Price: {old_price}\n"
        body += f"New Price: {new_price}\n\n"

    mail.send(to="originalhasyl@gmail.com",
              subject="Competitor Price Drop Alert",
              contents=body)
