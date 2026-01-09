# Username class
class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.music_collection = {}  # dictionary to store songs as title -> artist
        User.total_users += 1

    def add_song(self, title, artist):
        self.music_collection[title] = artist
        print(f"Added '{title}' by {artist} to {self.username}'s collection")

    def retrieve_song(self, title):
        return self.music_collection.get(title, "Song not found")

    def update_song(self, title, new_artist):
        if title in self.music_collection:
            self.music_collection[title] = new_artist
            print(f"Updated '{title}' to new artist '{new_artist}'")
        else:
            print("Song not found!")

    def delete_song(self, title):
        if title in self.music_collection:
            del self.music_collection[title]
            print(f"Deleted '{title}' from {self.username}'s collection")
        else:
            print("Song not found!")

    def display_songs(self):
        if not self.music_collection:
            print(f"No songs in {self.username}'s collection")
        else:
            print(f"Songs in {self.username}'s collection:")
            for title, artist in self.music_collection.items():
                print(f"{title} by {artist}")


# Song Class
class Song:
    total_songs = 0

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        Song.total_songs += 1


users = {}         # stores User objects
current_user = None



def add_user(username):
    global current_user
    if not username:
        print("No username entered!")
        return
    if username in users:
        print("User already exists!")
        return
    new_user = User(username)
    users[username] = new_user
    current_user = new_user
    print(f"User '{username}' added successfully!")


def change_user(username):
    global current_user
    if username in users:
        current_user = users[username]
        print(f"Switched to user '{username}'")
    else:
        print("User not found!")


def add_song_to_current_user(title, artist):
    if not current_user:
        print("No user selected!")
        return
    current_user.add_song(title, artist)


def retrieve_song_from_current_user(title):
    if not current_user:
        print("No user selected!")
        return
    artist = current_user.retrieve_song(title)
    print(f"{title}: {artist}")


def update_song_for_current_user(title, new_artist):
    if not current_user:
        print("No user selected!")
        return
    current_user.update_song(title, new_artist)


def delete_song_for_current_user(title):
    if not current_user:
        print("No user selected!")
        return
    current_user.delete_song(title)


def display_all_songs_for_current_user():
    if not current_user:
        print("No user selected!")
        return
    current_user.display_songs()


#Inserting the names and artists (attributes and methods)
    
# Add two users
add_user("Alexandre")
add_user("Cyrus")

# Add songs to Alexandre
add_song_to_current_user("La vie en rose", "Edith Piaf")
add_song_to_current_user("Smells like Teen Spirit", "Nirvana")
display_all_songs_for_current_user()

# Switch to Cyrus
change_user("Cyrus")
add_song_to_current_user("Volare", "Dean Martin")
display_all_songs_for_current_user()

# Update song for Cyrus
update_song_for_current_user("Volare", "Dean Martin")
retrieve_song_from_current_user("Volare")

# Delete song for Cyrus
delete_song_for_current_user("Volare")
display_all_songs_for_current_user()
