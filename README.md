# Blog Posts Rating App

The Blog Posts Rating App is a Django application that allows users to rate and manage blog posts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Issues](#Issues)
- [Areas for Improvement](#Areas-for-Improvement)

## Features

- **Rate Blog Posts**: Users can assign ratings to blog posts.
- **Manage Posts**: Add, edit, and delete blog posts. (from admin panel)
- **View Ratings**: Display average ratings and rating count for each post.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RezaQavi-Git/blog-posts-rating-app.git
   cd blog-posts-rating-app
   ```
2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:

   ```bash
   python3 blog_rating/manage.py runserver
   ```

## Issues

### 1. Post Rating Rate Limiting

A significant challenge in this system arises when a post receives a high volume of ratings (either very low or very high) within a short time. This can distort the average score and lead to inaccurate or fraudulent ratings. To address this issue, we can consider the following approaches:

- **Outlier Detection**:
  - Each rating can be evaluated individually by comparing its value to the standard deviation of the post's current average ratings. If the new rating is identified as an outlier, it can be temporarily ignored. When the user rates the post again, the system can re-evaluate and store the rating if it passes the validation criteria.

- **Batch Processing (Implemented in This Project)**:
  - A background job periodically recalculates the average score 
    of a post. This job processes ratings in batches, applying standardized metrics to filter and update the post's average score based on reliable data. This approach ensures that the final score is consistent and less prone to manipulation.

- **Rate Limiting:**
  - One of the key strategies to mitigate rating manipulation is implementing rate limiting. This ensures that users 
      cannot excessively rate a post within a short interval.

## Areas for Improvement

1. **Environment Management**:  
   Currently, environment variables are hardcoded in the project. In future iterations, these will be moved to a `.env` file and dynamically loaded into the project for better configuration management.  

2. **Database Storage**:  
   At this stage, the project uses Django's default database, a simple `sqlite` instance, to store post and rating data. In the future, this will be upgraded to a `PostgreSQL` database for improved scalability and performance. While `MongoDB` could be an alternative, our schema is static, making `PostgreSQL` the preferred choice.  

3. **Testing**:  
   Due to the simplicity of the current logic, comprehensive tests haven't been written yet. This is an area where improvements can be made as the project evolves.  

4. **Load Testing**:  
   A load testing phase is essential for evaluating the performance and accuracy of the average scoring logic. Tools like `Locust` or `k6` can be utilized for RESTful API load testing to ensure the system meets performance requirements.  
