#create the function
def calculate_discount(price, discount_percent):
   
   #alculate discount if it is 20% or higher 
   if discount_percent >=20:
      
      final_price = price - (price * (discount_percent /100))
      return final_price 
   else:
      return price 
   
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

#call function to alculate the final price 
final_price = calculate_discount(price, discount_percent)

if final_price < price:
   print(f"The final price after applying discount is: {final_price}")
else:
   print(f"No discount applied, The original price is: {price}")