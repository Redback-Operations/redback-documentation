---
sidebar_position: 8
sidebar_label: Local Setup Guide
---

# Setup documentation on local.

#### Prerequisites

-   **MSYS2 with mingw:** Or preferred Unix environment that can run shell scripts like `.sh` files.
    * **Download:** [https://www.msys2.org/](https://www.msys2.org/)
-   **Git:** For cloning the application.
    * **Download:** [https://git-scm.com/download/win](https://git-scm.com/download/win)
-   **Docker Desktop:** For running the backend service.
    * **Download:** [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
-   **Node.js and npm:**
    * **Download:** [https://nodejs.org/en/download](https://nodejs.org/en/download) (LTS version recommended)
-   **RedisInsight (optional):**
    * **Download:** [https://redis.io/downloads/#software](https://redis.com/downloads/redisinsight/)

1.  **Clone both the frontend and backend repositories** in the appropriate directory.
    * **Backend Repository:** `[e.g., git@github.com:bugboxau/PlayGround-backend.git]`
        * *(Tip: When cloning the backend on Windows, consider using `--config core.autocrlf=input` to help with script line endings: `git clone --config core.autocrlf=input [Backend Repo URL]`)`*
    * **Frontend Repository:** `[e.g., git@github.com:Redback-Operations/bugbox-redback-bugbox-main-playground.git]`

2.  **In MSYS2 `cd` into the appropriate backend directory** and run the backend service first with command:

    ```bash
    ./devtools/setup.sh
    ./devtools/start.sh
    ```

    This should be available at:
    `http://localhost:8090`

3.  **Install frontend dependencies** with:

    ```bash
    npm install
    ```

    If you encounter `npm ERR! gyp ERR! find VS` or other errors related to Visual Studio Build Tools, it means you need the "Desktop development with C++" workload installed via the [Visual Studio Installer](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022).

    If already installed in the appropriate frontend directory run:

    ```bash
    npm run dev
    ```

    The frontend will typically be accessible at:
    `http://localhost:3000`

The following is to install a tool called RedisInsight to easily access and inspect your local Redis QA database without needing command-line tools.

1.  **Open RedisInsight** while both the frontend and backend services are running.
2.  **Add a new Redis database connection** in RedisInsight using these details:
    * **Host:** `localhost`
    * **Port:** `6379`
    * **Password:** `bugbOxRedis@123`
    * *(Note: The container’s port is 6379. If prompted for a password, use `bugbOxRedis@123`.)*
