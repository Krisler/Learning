/*Data Structure Design:
Imagine you are designing a music player application,
and you want to manage a playlist of songs.
Each song in the playlist can be represented as a node in a singly linked list.*/

#include <iostream>
#include <string>

struct SongNode
{
    std::string title;
    std::string artist;
    SongNode *next;

    SongNode(std::string songTitle, std::string songArtist)
        : title(songTitle), artist(songArtist), next(nullptr) {}
};

// Playlist class using a singly linked list
class Playlist
{
private:
    SongNode *head;

public:
    Playlist() : head(nullptr) {}

    // Add a song to the end of the playlist
    void addSong(std::string title, std::string artist)
    {
        SongNode *newSong = new SongNode(title, artist);
        if (!head)
        {
            head = newSong;
        }
        else
        {
            SongNode *current = head;
            while (current->next)
            {
                current = current->next;
            }
            current->next = newSong;
        }
    }

    // Display the songs in the playlist
    void displayPlaylist()
    {
        SongNode *current = head;
        while (current)
        {
            std::cout << current->title << " by " << current->artist << std::endl;
            current = current->next;
        }
    }
};

int main()
{
    // Creating a playlist
    Playlist myPlaylist;

    // Adding songs to the playlist
    myPlaylist.addSong("Song A", "Artist X");
    myPlaylist.addSong("Song B", "Artist Y");
    myPlaylist.addSong("Song C", "Artist Z");

    // Displaying the playlist
    std::cout << "My Playlist:\n";
    myPlaylist.displayPlaylist();

    return 0;
}

/*
Explanation:
SongNode Structure:

The SongNode structure represents each song in the playlist. It contains fields for the song's title, artist, and a pointer to the next song in the playlist.
Playlist Class:

The Playlist class manages the playlist using a singly linked list. It includes methods for adding songs to the playlist and displaying the contents.
addSong Method:

The addSong method appends a new song to the end of the playlist. If the playlist is empty, the new song becomes the head. Otherwise, it traverses the list to find the last node and appends the new song.
displayPlaylist Method:

The displayPlaylist method prints the songs in the playlist by traversing the linked list.
*/