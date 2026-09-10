# Test Cases — Sauce Demo E-commerce Flow

Legend: **P** = Priority (High/Medium/Low)

## Login

| ID | Title | Preconditions | Steps | Expected Result | P |
|---|---|---|---|---|---|
| LOGIN-01 | Successful login with standard user | On login page | 1. Enter `standard_user` / `secret_sauce`<br>2. Click Login | User is redirected to the product listing page | High |
| LOGIN-02 | Login fails with invalid password | On login page | 1. Enter `standard_user` / `wrong_password`<br>2. Click Login | Error message is displayed; user stays on login page | High |
| LOGIN-03 | Login fails with locked-out user | On login page | 1. Enter `locked_out_user` / `secret_sauce`<br>2. Click Login | Error message indicates the user has been locked out | High |
| LOGIN-04 | Login fails with empty fields | On login page | 1. Leave username/password empty<br>2. Click Login | Error message indicates required field(s) missing | Medium |

## Product Listing

| ID | Title | Preconditions | Steps | Expected Result | P |
|---|---|---|---|---|---|
| PROD-01 | Product list loads with all items | Logged in as `standard_user` | 1. Observe product grid | All 6 products display with name, image, description, and price | High |
| PROD-02 | Sort products by price, low to high | Logged in as `standard_user` | 1. Select "Price (low to high)" from sort dropdown | Products reorder correctly by ascending price | Medium |
| PROD-03 | Sort products by name, A to Z | Logged in as `standard_user` | 1. Select "Name (A to Z)" from sort dropdown | Products reorder correctly alphabetically | Low |

## Cart

| ID | Title | Preconditions | Steps | Expected Result | P |
|---|---|---|---|---|---|
| CART-01 | Add single item to cart | Logged in, on product page | 1. Click "Add to cart" on any product | Cart icon badge shows "1"; button changes to "Remove" | High |
| CART-02 | Remove item from cart | Item already in cart | 1. Click "Remove" on the item | Cart badge count decreases; item no longer in cart | High |
| CART-03 | Cart badge reflects multiple items | Logged in, on product page | 1. Add 3 different items to cart | Cart badge shows "3" | Medium |
| CART-04 | Cart persists after navigating back | Item in cart | 1. Add item to cart<br>2. Go to cart page<br>3. Click "Continue Shopping" | Cart still shows the previously added item | Medium |

## Checkout

| ID | Title | Preconditions | Steps | Expected Result | P |
|---|---|---|---|---|---|
| CHK-01 | Complete checkout with valid info | At least 1 item in cart | 1. Go to cart → Checkout<br>2. Fill first name, last name, zip<br>3. Click Continue<br>4. Click Finish | Order confirmation page is displayed | High |
| CHK-02 | Checkout fails with missing required field | At least 1 item in cart | 1. Go to cart → Checkout<br>2. Leave "Zip/Postal Code" empty<br>3. Click Continue | Error message indicates the field is required; user stays on the form | High |
| CHK-03 | Checkout overview shows correct total | 2+ items in cart | 1. Proceed to checkout overview | Item total, tax, and total match the sum of item prices | High |
| CHK-04 | Cancel checkout returns to products | On checkout info page | 1. Click "Cancel" | User is redirected to product listing page | Low |
