from Skills.Acore import recognize_speech, speak, record_action
import feedparser
import webbrowser

# News
def read_unread_rss():
    try:
        # Load the RSS feed
        feed_url = 'https://feeds.bbci.co.uk/news/world/rss.xml'
        feed = feedparser.parse(feed_url)
        # Load previously read article IDs and spoken article IDs from separate files
        try:
            with open('Skills/CoreFiles/read_articles.txt', 'r') as f:
                read_article_ids = set(f.read().splitlines())
        except FileNotFoundError:
            read_article_ids = set()
        try:
            with open('spoken_articles.txt', 'r') as f:
                spoken_article_ids = set(f.read().splitlines())
        except FileNotFoundError:
            spoken_article_ids = set()
        # Check for unread articles
        unread_articles = []
        for entry in feed.entries:
            if entry.id not in read_article_ids and entry.id not in spoken_article_ids:
                unread_articles.append(entry)
        # Print out the unread articles
        if unread_articles:
            print(f'Found {len(unread_articles)} unread articles:')
            speak(f'Found {len(unread_articles)} unread articles:')
            for entry in unread_articles:
                print(f'Title: {entry.title} | Date: {entry.published} | Link: {entry.link} | Summary: {entry.summary}')
                speak(f'Title. {entry.title}. Date published. {entry.published}. Summary. {entry.summary}\n')
                record_action(f'News Read -  Title: {entry.title} | Link: {entry.link}')
                print('Would you like to read the next article?')
                speak('Would you like to read the next article?')
                decision = recognize_speech()
                if 'no' in decision:
                    spoken_article_ids.add(entry.id)
                    print('News reading ended')
                    speak('News reading ended')
                    break
                elif 'yes' in decision:
                    spoken_article_ids.add(entry.id)
        # Update the list of read article IDs and spoken article IDs
        with open('Skills/CoreFiles/read_articles.txt', 'a') as f:
            for entry in spoken_article_ids:
                f.write(entry + '\n')
        if not unread_articles:
            print('All articles have been read')
            speak('All articles have been read')
            print('Would you like to open BBC news?')
            speak('Would you like to open BBC news?')
            text = recognize_speech()
            if 'yes' in text:
                webbrowser.open('https://www.bbc.co.uk/news/world')
    except Exception as e:
        print("An error has occurred in the newsTeller command, output has been sent to errors.log")
        speak("An error has occurred in the newsTeller command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("read_unread_rss: " + str(e) + "\n")