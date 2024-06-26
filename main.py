import smtplib

PRODUCT_URL= "https://www.amazon.com/Nike-Waffle-Debut-DH9522001-Black/dp/B09NMHK4FC/ref=sxin_25_pa_sp_search_thematic_sspa?content-id=amzn1.sym.62c7b19e-4a44-4a87-90d6-fd9ab215d3f1%3Aamzn1.sym.62c7b19e-4a44-4a87-90d6-fd9ab215d3f1&crid=1HRFMKX38EYL8&cv_ct_cx=nike+shoes+men&dib=eyJ2IjoiMSJ9.CCcFGpbuIJ68Q4FEa7FSc5z4TceyhA2RzNC8dfZz7RAnPWmhpDf8YQN6p-EjhCB0PHn16v54AkVc9HZNLic-Yw.YTOkPtHac3H5HBBfYLjmTb8NUiNGw-2LgzfueWci0Io&dib_tag=se&keywords=nike+shoes+men&pd_rd_i=B09NMHK4FC&pd_rd_r=194312b9-4933-4ba0-9a0d-2730ed496d76&pd_rd_w=kWjgV&pd_rd_wg=oAfBB&pf_rd_p=62c7b19e-4a44-4a87-90d6-fd9ab215d3f1&pf_rd_r=5XHQ53CCDKXP6WVMP6PB&qid=1718087945&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=nike%2Caps%2C495&sr=1-2-320c8157-e12c-4633-a9a3-0e0d4c4cb4b0-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1"

header = { 'Accept-Language' :'en-US,en;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

from bs4 import BeautifulSoup
import requests
import lxml

response= requests.get(PRODUCT_URL, headers=header)
# soup= BeautifulSoup(response.text, "html.parser")
#
# price_of_product= soup.find(name="span", class_="a-offscreen")
# print(price_of_product.text)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float<70.00:
    #sending email to notify the drop down of the price of product
    my_email = "vishnurao443@gmail.com"
    password = "nueo vbea hpfa zfha"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nikkitasahu335@gmail.com",
                            msg=f"subject:Product Price reduced. \n\n The Nike basketball shoes price is reduced to{price_as_float} and the link is {PRODUCT_URL}"
                            )

# title = soup.find(id="productTitle").get_text().strip()
# print(title)
#
# BUY_PRICE = 71
#
# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"
#
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         result = connection.login("vishnurao443@gmail.com", "nueo vbea hpfa zfha")
#         connection.sendmail(
#             from_addr="vishnurao443@gmail.com",
#             to_addrs="nikkitasahu335@gmail.com",
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
#         )