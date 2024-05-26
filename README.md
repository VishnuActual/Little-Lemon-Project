# Little Lemon Restaurant API Project

## Introduction

This document provides an overview of the scope of the Little Lemon restaurant API project, including all necessary endpoints and implementation notes. It serves as a guide to successfully completing the project and should be referenced during development to ensure adherence to project requirements.

## Scope

The project entails creating a fully functioning API for the Little Lemon restaurant. This API will enable client application developers to develop web and mobile applications. Users with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crews to orders, and deliver orders.

## Structure

The API project will consist of a single Django app called LittleLemonAPI, where all API endpoints will be implemented. Dependencies will be managed using pipenv. Refer to the video on creating a Django project using pipenv for guidance.

## Function or Class-Based Views

Both function- and class-based views can be utilized in this project. It's essential to follow proper API naming conventions throughout the project. Review the videos on function- and class-based views as well as naming conventions for guidance.

## User Groups

Two user groups, Manager and Delivery Crew, will be created. Users not assigned to a group will be considered customers. Refer to the video on user roles for guidance.

## Error Check and Proper Status Codes

Error messages with appropriate HTTP status codes will be displayed for specific errors. Refer to the provided list of HTTP status codes and their corresponding reasons for guidance.

## API Endpoints

The following sections outline the required API routes for this project, grouped into several categories.

### User Registration and Token Generation Endpoints

#### `/api/users`
- **Role**: No role required
- **Method**: POST
- **Purpose**: Creates a new user with name, email, and password.

#### `/api/users/me/`
- **Role**: Anyone with a valid user token
- **Method**: GET
- **Purpose**: Displays only the current user.

#### `/token/login/`
- **Role**: Anyone with a valid username and password
- **Method**: POST
- **Purpose**: Generates access tokens for use in other API calls.

### Menu-Items Endpoints

#### `/api/menu-items`
- **Role**: Customer, delivery crew
- **Method**: GET
- **Purpose**: Lists all menu items.

... (continue adding endpoints following the provided structure)

### User Group Management Endpoints
### User Group Management Endpoints

#### `/api/groups/manager/users`
- **Role**: Manager
- **Method**: GET
- **Purpose**: Returns all managers.

#### `/api/groups/manager/users`
- **Role**: Manager
- **Method**: POST
- **Purpose**: Assigns the user in the payload to the manager group. Returns 201-Created.

#### `/api/groups/manager/users/{userId}`
- **Role**: Manager
- **Method**: DELETE
- **Purpose**: Removes the specified user from the manager group. Returns 200-Success if successful, 404-Not found if the user is not found.

#### `/api/groups/delivery-crew/users`
- **Role**: Manager
- **Method**: GET
- **Purpose**: Returns all delivery crew.

#### `/api/groups/delivery-crew/users`
- **Role**: Manager
- **Method**: POST
- **Purpose**: Assigns the user in the payload to the delivery crew group. Returns 201-Created.

#### `/api/groups/delivery-crew/users/{userId}`
- **Role**: Manager
- **Method**: DELETE
- **Purpose**: Removes the specified user from the delivery crew group. Returns 200-Success if successful, 404-Not found if the user is not found.


### Cart Management Endpoints

#### `/api/cart/menu-items`
- **Role**: Customer
- **Method**: GET
- **Purpose**: Returns current items in the cart for the current user token.

#### `/api/cart/menu-items`
- **Role**: Customer
- **Method**: POST
- **Purpose**: Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items.

#### `/api/cart/menu-items`
- **Role**: Customer
- **Method**: DELETE
- **Purpose**: Deletes all menu items created by the current user token.

### Order Management Endpoints

#### `/api/orders`
- **Role**: Customer
- **Method**: GET
- **Purpose**: Returns all orders with order items created by the current user.

#### `/api/orders`
- **Role**: Customer
- **Method**: POST
- **Purpose**: Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.

#### `/api/orders/{orderId}`
- **Role**: Customer
- **Method**: GET
- **Purpose**: Returns all items for the specified order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.

#### `/api/orders`
- **Role**: Manager
- **Method**: GET
- **Purpose**: Returns all orders with order items by all users.

#### `/api/orders/{orderId}`
- **Role**: Customer
- **Method**: PUT, PATCH
- **Purpose**: Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1. If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery. If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered.

#### `/api/orders/{orderId}`
- **Role**: Manager
- **Method**: DELETE
- **Purpose**: Deletes the specified order.

#### `/api/orders`
- **Role**: Delivery crew
- **Method**: GET
- **Purpose**: Returns all orders with order items assigned to the delivery crew.

#### `/api/orders/{orderId}`
- **Role**: Delivery crew
- **Method**: PATCH
- **Purpose**: Updates the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.


