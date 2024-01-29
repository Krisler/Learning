#include <iostream>
#include <string>

// Node structure representing a visited web page
struct WebPageNode
{
    std::string url;
    std::string title;
    WebPageNode *prev;
    WebPageNode *next;

    WebPageNode(std::string pageUrl, std::string pageTitle)
        : url(pageUrl), title(pageTitle), prev(nullptr), next(nullptr) {}
};

// BrowserHistory class using a doubly linked list
class BrowserHistory
{
private:
    WebPageNode *current;

public:
    BrowserHistory() : current(nullptr) {}

    // Visit a new web page and add it to the history
    void visitPage(std::string url, std::string title)
    {
        WebPageNode *newPage = new WebPageNode(url, title);

        if (!current)
        {
            current = newPage;
        }
        else
        {
            newPage->prev = current;
            current->next = newPage;
            current = newPage;
        }
    }

    // Navigate to the previous web page
    void goBack()
    {
        if (current && current->prev)
        {
            current = current->prev;
        }
    }

    // Navigate to the next web page
    void goForward()
    {
        if (current && current->next)
        {
            current = current->next;
        }
    }

    // Display the current web page
    void displayCurrentPage()
    {
        if (current)
        {
            std::cout << "Current Page: " << current->title << " (" << current->url << ")\n";
        }
        else
        {
            std::cout << "No page currently visited.\n";
        }
    }
};

int main()
{
    // Creating a browser history
    BrowserHistory myHistory;

    // Visiting web pages
    myHistory.visitPage("https://www.example.com", "Example Website");
    myHistory.visitPage("https://www.google.com", "Google Search");
    myHistory.visitPage("https://www.wikipedia.org", "Wikipedia");

    // Displaying the current page
    myHistory.displayCurrentPage();

    // Navigating backward
    myHistory.goBack();
    myHistory.displayCurrentPage();

    // Navigating forward
    myHistory.goForward();
    myHistory.displayCurrentPage();

    return 0;
}
