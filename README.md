# Alethea MLE Take Home Assignment

## Description
This project is a solution to Alethea's MLE Take Home Assignment. It includes Python scripts for processing COVID-19 related posts and accounts data. The goal is to identify accounts that posted a specific hashtag and have similar screen names.

## Data
The project uses two datasets, `posts.tsv` and `accounts.tsv`, containing information about posts and accounts related to COVID-19 in December 2023.

### Posts
- **id:** The unique identifier of the post.
- **created_at:** The time at which the post was made.
- **author_id:** The ID of the account that made the post.
- **is_repost:** Whether the post is a repost.
- **text:** The text of the post.
- **hashtags:** The unique hashtags present in the post, each separated by a pipe `|`.

### Accounts
- **id:** The unique identifier of the account.
- **created_at:** The time at which the account was made.
- **screen_name:** The screen name of the account, also known as its handle or username.

## Installation and Setup locally
1. Clone the repository to your local machine.
2. Download the data by running the following commands:
   ```bash
   wget https://alethea-take-home.s3.amazonaws.com/posts.tsv
   wget https://alethea-take-home.s3.amazonaws.com/accounts.tsv


3. Ensure you have Python installed.
4. Install the required dependencies by running:
    ```
    cd <root of project>
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
5. Start the Flask server by running:
    ```
    source .venv/bin/activate (if required)
    ./scripts/run.sh
    ```
6. Access the API endpoint using a web browser or a tool like Postman:

    ```
    GET http://127.0.0.1:8080/api/get_similar_accounts?hashtag=YOUR_HASH_TAG&min_similarity=0.8
    ```

    Replace `YOUR_LATITUDE`  with the desired hashtag values like diedsuddenly.
## Dockerization and Deployment

Assuming your application is already dockerized, you can follow these steps to create a Docker image from the Dockerfile and run the app on port 8080:

1. **Build Docker Image:**
   - Open a terminal and navigate to the root directory of your application.
   - Run the following command to build the Docker image:

     ```bash
     docker build -t your-app-image:latest .
     ```

   - This command assumes your Dockerfile is named `Dockerfile`. Replace `your-app-image` with a suitable name for your Docker image.

2. **Run Docker Container:**
   - After successfully building the Docker image, run the following command to start a Docker container:

     ```bash
     docker run -p 8080:8080 -d your-app-image:latest
     ```

   - The `-p 8080:8080` option maps port 8080 on the host to port 8080 in the container.
   - Replace `your-app-image` with the same name you used during image creation.

3. **Verify Running Container:**
   - To verify that the Docker container is running, execute:

     ```bash
     docker ps
     ```

   - You should see an entry for your running container.

4. **Access the App:**
   - Open a web browser or a tool like Postman.
   - Access the app by navigating to `http://localhost:8080` in the browser or using the appropriate API endpoint.

Now, your app should be up and running within a Docker container on port 8080.

**Additional Notes:**
- Ensure that there are no other services running on port 8080 on your host machine to avoid conflicts.
- Adjust the Dockerfile or the `docker run` command if your application requires specific configurations.
- These instructions assume a basic setup and might need adjustments based on your application's specific requirements.
- Monitor logs using `docker logs <container_id>` to troubleshoot any issues during the container startup.

## API Endpoint
- **Endpoint:** `/api/get_similar_accounts`
- **Method:** GET
- **Parameters:**
    - `hashtag` (required): The hashtag to filter posts and identify similar accounts.
    - `min_similarity` (optional): Minimum similarity threshold for identifying similar accounts (default is 0.8).
- **Response:**
    - If successful, returns a JSON object containing an array of similar account pairs with their similarity scores:

    ```json
    {
        "similar_account_pairs": [
            ["35a03c48-c8e0-4e7a-8437-acfa2aae8212", "3705f1d8-2b1a-4c43-b2dc-58d8fe7f646f", 0.9333333333333333],
            ["35a03c48-c8e0-4e7a-8437-acfa2aae8212", "e0e8c80a-8712-400c-934e-6a430c136c6d", 0.9333333333333333],
            // ... (other similar account pairs)
        ]
    }
    ```
    - Each similar account pair consists of two account IDs and their similarity score.
    - If there are no similar accounts or if the provided hashtag is not found, an empty array will be returned.

## Additional Notes
- The `min_similarity` parameter is optional, and the default value is set to 0.8 if not provided.
- The response provides account pairs that have similarity scores above the specified threshold.
- Error handling is implemented to handle cases such as missing or invalid parameters.
- This implementation is designed for demonstration purposes and may require additional enhancements for production use, such as security measures, scalability considerations, and performance optimizations.

