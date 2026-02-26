from pymongo import MongoClient

client =MongoClient("mongodb+srv://sahanilesh:Nilesh123@cluster0.37ilghf.mongodb.net/")
db = client["youtube_manager"]
videos_collection = db["videos"]
print(videos_collection)

def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Length: {video['length']}")

def add_video(name, length):
    videos_collection.insert_one({"name": name, "length": length})

def update_video(video_id, new_name, new_length):
    videos_collection.update_one({"_id": video_id}, {"$set": {"name": new_name, "length": new_length}})

def delete_video(video_id):
    videos_collection.delete_one({"_id": video_id})


def main():
    while True:
        print("\nYoutube Manager")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            length = input("Enter video length : ")
            add_video(name, length)
        elif choice =="3":
            video_id = input("Enter video ID to update: ")
            new_name = input("Enter new video name: ")
            new_length = input("Enter new video length: ")
            update_video(video_id, new_name, new_length)
        elif choice =="4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice =="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()