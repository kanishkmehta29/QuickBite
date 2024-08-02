# QuickBite
This project is a web-based food ordering system designed for hostel canteens and food services at IIT Guwahati. The system allows users to place orders for various food items from different food outlets within the campus.

# Tech-Stack Used
The Food Ordering website - QuickBite is built using [Django](https://www.djangoproject.com/), a high-level Python web framework known for its scalability and robustness. The project also utilizes HTML and Bootstrap for front-end development, and incorporates a relational database management system [SQLite3](https://www.sqlite.org/index.html) to handle data storage efficiently.

# Features
* The website incorporates user authentication for logging in and logging out, and it includes <b>email verification</b> as part of the signing up process.
* Features menus from multiple food outlets across the campus, allowing users to order food conveniently from a variety of options in one place.
* Provides a user-friendly experience by categorizing menus from various food outlets into intuitive <b>sections</b> and <b>subsections</b>, allowing users to quickly find and browse through their preferred cuisine options
* Acess restriction based on user types.

* **Features for Registered Users:**
  - The website offers a straightforward and user-friendly process for ordering items from any food outlet.
  - Users can easily track their **Current Order** and view their **Order Logs** to stay informed about the delivery status of their orders and access their previous orders.
  - Receive **email notifications** upon placing an order and upon its delivery, ensuring they are updated throughout the ordering process.
  
* **Features for Food Outlet Users:**
  - Owners can easily update their menus using a simple and intuitive process organized into sections and subsections.
  - Owners can view the orders that have been placed, including their delivery status, in the **Orders Received** section.
  - Receive **email notifications** whenever an order is placed.
  - Update the delivery status of orders to ensure customers receive notifications and maintain accuracy.
 
# Website(Visuals)
* <b> Home Page </b>:</br>

![homepage](https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/homepage.png)</br></br>

* <b> Login and Signup Pages </b>:</br>

<p align="center">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/login.png" height="300" width="45%"/>
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/signup.png" height="300" width="45%"/>
</p>
* <b> Email Verification </b>:</br>

<p align = "center" style="margin: 70px; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/emailverificationnew.png" alt="featureimage" height="300"/>
</p>
* <b> FoodOutlet Display </b>:</br>

![homepage](https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/foodoutlets.png)</br></br></br>
* <b> Addfoodsection (only visible to staff) </b>:</br>

<p align = "center" style="margin: 70px; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/addfoodoutlet.png" alt="featureimage" height="300"/>
</p>


* <b> Menu (Divided into sections) : Lohit Canteen(Example) </b></br></br>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/snacks.png" alt="image3" height="300"/>
</div>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/maincourse.png" alt="image3" height="300"/>
</div>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/beverages.png" alt="image3" height="300"/>
</div>

* <b> Subsections (Example shown for section 'Chaat_Items' in Lohit Canteen) </b>:</br>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/subsections.png" alt="image3" height="300"/>
</div>
</br>

*  <b> Addsection and Addsubsection options(* only visible to respective outlet owners ) </br></br>
  <p align="center">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/addsection.png" height="300" width="45%"/>
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/addsubsection.png" height="300" width="45%"/>
</p>
</br>

*  <b> Users can order items by simply clicking 'order' in the subsection of their choice </b></br></br></br>

* <b> Current Order and Order Confirmation Pages </b></br></br>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/currentorder.png" alt="image3" height="300"/>
</div>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/orderconfirmation.png" alt="image3" height="450"  />
</div>
</br>

* <b> OrderLogs (Deliverd(Blue) and Active(Green) orders)</b>:</br>
<p align="center">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/orderlogprevnew.png" height="500" width="45%"/>
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/orderlogcurr.png" height="500" width="50%" style="object-fit: cover;"/>
</p>
</br>

* <b> Email Notifications on Placing and Receiving Orders </b>:</br>
<p align="center">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/ordersplacednew.png" height="300" width="45%"/>
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/orderdelivedrednew.png" height="300" width="45%"/>
</p>
</br>

* <b> OrderReceived(Visible to Respective Outlet Ownners) (Deliverd(Blue) and Due(Yellow) orders)</b>:</br></br></br>
<p align="center">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/ordersreceivedlognew.png" height="500" width="45%"/>
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/ordersrecievedcurr.png" height="500" width="50%" style="object-fit: cover;"/>
</p>
</br>

* <b> Outlet  owners can just click 'Delivered' to update the status and send notification to customers </b></br>
</br>

* <b> Access Denied Page (on visiting restricted pages like accessing some other users orders etc ..) </b></br>
<div align = "center" style="display: flex; justify-content: center; margin-top: 20px;">
  <img src="https://github.com/chandrashekhar14d/QuickBite/blob/main/quickbiteimages/accessdeneid.png" alt="image3" height="300"/>
</div>



# Team:

 **This Project was made By :**
   - [Chandrashekhar Dharmarajan](https://github.com/chandrashekhar14d)
   - [Kanishk Mehta](https://github.com/kanishkmehta29)
