# Event Manager Web App

Welcome to the Event Manager Web App! This web application is designed to help users manage events, promoters, venues, and also features a social media-like feed where users can post, like, and comment on pictures from events. Additionally, it includes a calendar for viewing and managing events.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Visit Demo App](https://evntmngr.xyz)

## Features

### Event Management
- Create, edit, and delete events.
- View events on a calendar.
- Manage event details, including date, time, venue, and description.
- Categorize events by type, genre, or any custom criteria.

### Promoter Management
- Add, edit, and delete promoters.
- Associate promoters with events.
- Keep track of promoter information, contact details, and events they are involved in.

### Venue Management
- Maintain a list of venues and their details.
- Link venues to events for easy access.
- Store venue addresses, contact information, and capacity.

### Social Media-Like Feed
- Allow users to post pictures from events.
- Users can like and comment on posted pictures.
- Create a vibrant community around the events.

### User Accounts
- User registration and authentication.
- User profiles with customizable information.
- Permission-based access control for managing events, promoters, and venues.

## Getting Started

To get started with the Event Manager Web App, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies (see [Installation](#installation) below).
3. Set up your Django environment, database, and configure your settings.
4. Migrate the database schema.
5. Run the development server and access the app in your browser.

## Installation

1. **Python and Django**:
   - Make sure you have Python installed. This project was developed with Python 3.11.+ and Django 5.1.

2. **Clone the Repository**:

```bash
git clone https://github.com/jackjakarta/eventManager
```

3. **Create and activate a new python environment to install your dependencies:**
```bash
python3 -m venv env
source env/bin/activate
```

4. **Install Dependencies:**

```bash
pip3 install -r requirements.txt
```

5. **Database Setup:**
- Configure your database settings in `settings.py`.
- Migrate the tables to your new db:
  ```bash
  python3 manage.py migrate
  ```

6. **Configure ENV variables:**
- Set up your environment variables using the template at `.env.default`

7. **Run the Development Server:**

```bash
python3 manage.py runserver
```

8. Access the app in your browser at [http://localhost:8000](http://localhost:8000).

## API Endpoints

The Event Manager Web App provides a set of API endpoints to interact with its features programmatically. These endpoints allow developers to access and manipulate data related to venues, events, artists, promoters, and more. You can access these endpoints at [http://localhost:8000/api/](http://localhost:8000/api/).

### Authentication

Authentication is required for accessing various endpoints in the Event Manager Web App's API. While **GET** requests to most endpoints are public and do not require authentication, other HTTP methods like **POST**, **PUT**, and **DELETE** require either an ***API Key*** or ***JWT (JSON Web Token)*** authentication.

To obtain a JWT token pair for authentication, users can visit the `/auth` endpoint, which provides a way to generate tokens securely. Additionally, in case of token expiration or security concerns, users can reset their JWT tokens at the `/auth/reset` endpoint.

Authentication ensures that only authorized users have access to create, modify, or delete data through the API, enhancing the security and control of the Event Manager Web App.

Here are some of the available API endpoints:

### Events
- **List Events:** `GET /api/events/` - Retrieve a list of all events.
- **Create Event:** `POST /api/events/` - Create a new event.
- **Retrieve Event:** `GET /api/events/{event_id}/` - Retrieve details of a specific event.
- **Update Event:** `PUT /api/events/{event_id}/` - Update event details.
- **Delete Event:** `DELETE /api/events/{event_id}/` - Delete a specific event.

### Promoters
- **List Promoters:** `GET /api/promoters/` - Retrieve a list of all promoters.
- **Create Promoter:** `POST /api/promoters/` - Create a new promoter.
- **Retrieve Promoter:** `GET /api/promoters/{promoter_id}/` - Retrieve details of a specific promoter.
- **Update Promoter:** `PUT /api/promoters/{promoter_id}/` - Update promoter details.
- **Delete Promoter:** `DELETE /api/promoters/{promoter_id}/` - Delete a specific promoter.

### Venues
- **List Venues:** `GET /api/venues/` - Retrieve a list of all venues.
- **Create Venue:** `POST /api/venues/` - Create a new venue.
- **Retrieve Venue:** `GET /api/venues/{venue_id}/` - Retrieve details of a specific venue.
- **Update Venue:** `PUT /api/venues/{venue_id}/` - Update venue details.
- **Delete Venue:** `DELETE /api/venues/{venue_id}/` - Delete a specific venue.

### Artists
- **List Artists:** `GET /api/artists/` - Retrieve a list of all artists.
- **Create Artist:** `POST /api/artists/` - Create a new artist.
- **Retrieve Artist:** `GET /api/artists/{artist_id}/` - Retrieve details of a specific artist.
- **Update Artist:** `PUT /api/artists/{artist_id}/` - Update artist details.
- **Delete Artist:** `DELETE /api/artists/{artist_id}/` - Delete a specific artist.

### Social Media Feed
- **List Posts:** `GET /api/posts/` - Retrieve a list of all social media posts.
- **Create Post:** `POST /api/posts/` - Create a new social media post.
- **Retrieve Post:** `GET /api/posts/{post_id}/` - Retrieve details of a specific social media post.
- **Delete Post:** `DELETE /api/posts/{post_id}/` - Delete a specific social media post.

These API endpoints provide a convenient way to integrate the Event Manager Web App's functionality into your own applications or services. You can make HTTP requests to these endpoints to perform CRUD (Create, Read, Update, Delete) operations on events, promoters, venues, artists, and social media posts.


## Usage

Once the application is running, you can start managing events, promoters, venues, and using the social media-like feed. Users can register, log in, and enjoy the features provided by the Event Manager Web App.

## Technologies Used

- Django
- Django REST Framework
- MySQL
- HTML/CSS
- Bootstrap
