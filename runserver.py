import sys
import uvicorn


if __name__ == "__main__":
    # Set working directory path
    sys.path.insert(0, "be")

    # Run uvicorn
    uvicorn.run("app:server", host="127.0.0.1", port=5000, log_level="info", reload=True)
