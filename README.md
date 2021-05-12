# marketDemo

## Outline
### Landing Pages - Unprotected
Sign in / Sign up
Both land the user to the Protected route of Dashboard

### Protected Routes
#### Dashboard -
    Has all products in database listed
#### Categories -
    View products by category via JS and dropdowns
#### Shops - 
    View products by shop via JS and dropdowns
#### Profile -
    Shows current user profile information - routes to update information and delete account (will redirect back to login)
    Have Navigation to add/edit/delete Categories, Shop name, Products

### Register Requirements - 1:1
username
password
firstName
lastName
email

### Shop Requirements 1:Many (User)
shopName
shopDescription
shopLocation (for stretch of cart and thus shipping)
shopOwner

### Category Requirements Many:Many (Product)
catName
assignedProd

### Product Requirements 1:Many (Shop, Category)
itemName
itemDescription
itemPrice
itemImg
itemCount
itemShop

### Defaults
Category Default - General Product
Shop Defaults - Main Shop