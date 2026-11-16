Markdown
# Film Catalog Web Application

A lightweight, full-stack Python web application built with the **Bottle** micro-framework and **SQLite**. The application implements session-based user authentication via timed browser cookies, role/year-filtered database queries, and full CRUD capabilities for managing a movie catalog.

---

## Overview

This web service allows authenticated users to view, add, and remove films stored in a relational SQLite database (`movies5.db`). Upon logging in, users are assigned an expiring session cookie tied to a specific release year, dynamically scoping their catalog views and newly created entries to that year.

---

## Key Technical Highlights

* **Stateful Session Management:** Implements browser cookie authentication (`response.set_cookie`) with a 5-minute (`max_age=300`) expiration window, enforcing session validation across protected routes and providing clean session termination on logout.
* **Relational Database Integration:** Executes multi-table `SELECT` joins across `films` and `categories` tables alongside parameterized `INSERT` and `DELETE` statements (`?` placeholders) to prevent SQL injection.
* **RESTful Routing & HTTP Method Handling:** Maps distinct `GET` and `POST` handlers using Bottle's `@route` decorators to separate form rendering from form submission processing[cite: 2].
* **Server-Side Validation:** Verifies active session cookies and validates required form fields prior to executing database mutations[cite: 2].

---

## Tech Stack

* **Language:** Python 3[cite: 2]
* **Web Framework:** [Bottle](https://bottlepy.org/) (`bottle`)[cite: 2]
* **Database:** SQLite (`sqlite3`)[cite: 2]
* **Templating:** Bottle SimpleTemplate Engine (`.tpl` views)[cite: 2]

---

## API Routes & Endpoints

| Endpoint | Methods | Auth Required | Description |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | No | Renders the initial user login view (`index`)[cite: 2]. |
| `/login` | `GET`, `POST` | No | Authenticates credentials against the `users` table, sets a 300-second `year` cookie, and loads the `main menu` template[cite: 2]. |
| `/logout` | `GET`, `POST` | No | Clears the active `year` session cookie and redirects to `/`[cite: 2]. |
| `/showallmovies` | `GET` | Yes | Joins `films` and `categories` filtered by the user's cookie `year` and renders `displayfilms`[cite: 2]. |
| `/addmovie` | `GET`, `POST` | Yes | Renders the `add_movie` form (`GET`) or inserts a new film scoped to the user's `year` cookie (`POST`)[cite: 2]. |
| `/rem_movie` | `GET`, `POST` | Yes | Renders the `rem_movie` form (`GET`) or deletes a record matching both `film_id` and `title` (`POST`)[cite: 2]. |

---

## Getting Started

### Prerequisites

* Python 3.x[cite: 2]
* `bottle` web framework[cite: 2]

bash
pip install bottle
Project Structure
Ensure your working directory includes the application script, SQLite database, and Bottle HTML templates (inside a /views folder):

Plaintext
├── index.py
├── movies5.db
└── views/
    ├── index.tpl
    ├── main menu.tpl
    ├── displayfilms.tpl
    ├── add_movie.tpl
    ├── rem_movie.tpl
    ├── message.tpl
    └── message_2.tpl
Database Schema
The application expects movies5.db to contain users, categories, and films tables[cite: 2]:

SQL
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    year TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    category INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS films (
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    release_year TEXT NOT NULL,
    length INTEGER,
    category INTEGER,
    FOREIGN KEY (category) REFERENCES categories(category)
);
Running the Server
Start the local web server on port 8083[cite: 2]:

Bash
python index.py
Open a browser and navigate to http://localhost:8083[cite: 2]
