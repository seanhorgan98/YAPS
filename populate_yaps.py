import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'yaps_project.settings')

import django
django.setup()
from YAPS.models import Category, Podcast

def populate():
 # First, we will create lists of dictionaries containing the pages
 # we want to add into each category.
 # Then we will create a dictionary of dictionaries for our categories.
 # This might seem a little bit confusing, but it allows us to iterate
 # through each data structure, and add the data to our models.

    sport_podcasts = [
        {"title": "The euro league football show",
         "publish_date":"26/03/2018",
         "url":"https://www.bbc.co.uk/programmes/p062f3yc",
         "duration_mins":"46",
         "RSS_feed":"http://podcasts.files.bbci.co.uk/b0940sk5.rss",
         "category":"Sport",
         "description":"How are the top teams shaping up ahead of the World Cup? Euro Leagues Football Show The team discuss how the likes of Germany, Spain and France are preparing for theWorld Cup and also talk about the rumours surrounding Thomas Tuchel and Arsenal"
                        },
        {"title":"Rugby union weekly",
        "publish_date":"26/03/2018",
        "url":"https://www.bbc.co.uk/programmes/p062dtx3",
        "duration_mins":"61",
        "RSS_feed":"http://podcasts.files.bbci.co.uk/p04q5p2n.rss",
        "category":"Sport",
        "description":"Jamie Heaslip and the suede boot drop-goal .Rugby Union Weekly Ugo and Chris speak to Ireland legend Jamie Heaslip about missing out on the grand slam, his ten trips to Las Vegas and why he loves working with Stuart Lancaster. Ugo is keen to mention his London stadium drop goal, but there are serious issues to discuss after Nick Kennedy is “forced out” of London Irish and Chris is “forced in” to a London museum."
         },
        {"title":"radio hibs. the final whistle st johnstone",
         "publish_date":"16/03/2018",
         "url":"https://player.fm/series/radio-hibs",
        "duration_mins":"37",
         "RSS_feed":"http://podcasts.files.bbci.co.uk/p04q5p2n.rss",
         "category":"Sport",
         "description":"Danny Galbraith joins Daniel Waterson and James Delaney to discuss Hibs 1-1 draw with St Johnstone in Perth. Cliff Pike gets post match reaction from Neil Lennon and Cammy Bell"
         } ]

    comedy_podcasts = [
        {"title":"Rhod gilberts best bits: the ant festival",
        "publish_date":"24/03/2018",
        "url":"https://www.bbc.co.uk/programmes/p0626pc0",
        "duration_mins":"34",
        "RSS_feed":"http://podcasts.files.bbci.co.uk/p02nrsrr.rss",
        "category":"Comedy",
        "description":"Rhod and Ed Gamble argue over pears while Sian Harries imagines an insect music festival."
         },
        {"title":"No Pressure To Be Funny:",
        "publish_date":"28/06/2015",
        "url":"https://www.comedy.co.uk/podcasts/no_pressure_to_be_funny/28_06_2015/",
        "duration_mins":"98",
        "RSS_feed":"http://feeds.feedburner.com/NoPressureToBeFunny",
        "category":"Comedy",
        "description":"This month, Omid Djalili, Sajeela Kershi, Chris Neill and Jake Yapp discuss, amongst other things, rock festivals, royalty, torture, peaceful protest, women's football and The Comedy Godfather, Barry Cryer. Masterful musical sets from Ronnie Golden, and hosted by Nick Revell."
          },
        {"title":"The Now Show - Series 52 Episode 4",
         "publish_date":"23/06/2018",
         "url":"https://www.bbc.co.uk/programmes/p0623tzj",
        "duration_mins":"30",
         "RSS_feed":"http://podcasts.files.bbci.co.uk/p02pc9pj.rss",
         "category":"Comedy",
         "description":"Steve Punt, Hugh Dennis and guests Gemma Arrowsmith, Marcus Brigstocke, Jess Robinson and Ahir Shah present the week via topical stand-up and sketches."
         } ]
    
    drama_podcasts = [
         {
          "title":"the archers",
          "publish_date":"11/06/2018",
          "url":"https://www.bbc.co.uk/programmes/b09tyzh2",
          "duration_mins":"75",
          "RSS_feed":"http://podcasts.files.bbci.co.uk/b006qnkc.rss",
          "category":"Drama",
          "description":"Will comes to a decision, and Kate returns to Ambridge."
          },
          {
           "title":"The Unforgiven Episode 5",
           "publish_date":"09/06/2018",
           "url":"https://www.bbc.co.uk/programmes/p060j886",
           "duration_mins":"45",
           "RSS_feed":"http://podcasts.files.bbci.co.uk/p06080gh.rss",
           "category":"Drama",
           "description":"With one day left to save Boyd and crack the case, everything disappears into desperation as another victim is snatched, right from under our team."
                },
          {
           "title":"The war horse Episode 10",
           "publish_date":"25/06/2018",
           "url":"https://www.bbc.co.uk/programmes/p04rs4j3",
           "duration_mins":"16",
           "RSS_feed":"http://podcasts.files.bbci.co.uk/p04rs0qr.rss",
           "category":"Drama",
           "description":"The War finally comes to an end but the army decides the horses, including Joey, will be sold at auction in France. What can Albert and the other soldiers do to save him?"
}           
         ]
    music_podcasts = [
         {
        "title":"A-Z of punk:",
        "publish_date":"20/10/2017",
        "url":"https://www.bbc.co.uk/programmes/p05kggss",
        "duration_mins":"18",
        "RSS_feed":"http://podcasts.files.bbci.co.uk/p05k8003.rss",
        "category":"Music",
        "description":"Stories from the notorious Anarchy Tour in 1976, how watching The Sex Pistols inspired Stuart Goddard to form Adam and the Ants and ‘One Chord Wonders’ The Adverts get a deserved mention."
         },
        {
        "title":"The JogTunes Indie Podcast",
        "publish_date":"01/03/2018",
        "url":"https://player.fm/series/the-jogtunes-indie-podcast/ep-150-37-min-146-165-light-and-easy",
        "duration_mins":"37",
        "RSS_feed":"http://feeds.feedburner.com/jogtunesindie",
        "category":"Music",
        "description":"The 150th episode of the JTIP featuring Esme Bridie and seven other great indie artists."
         },
         {
        "title":"Scotland introducing",
        "publish_date":"23/03/2018",
        "url":"https://www.bbc.co.uk/programmes/p061zkdl",
        "duration_mins":"13",
        "RSS_feed":"http://podcasts.files.bbci.co.uk/p02nrw8p.rss",
        "category":"Music",
        "description":"Vic Galloway with fresh new music. Scotland Introducing Vic playes new music from Beta Waves, Heavy Rapids, The Rotations and Flux Velociraptor."
         } ]
    
    cats = {"Sport": {"podcasts": sport_podcasts, },
        "Comedy": {"podcasts": comedy_podcasts, },
        "Drama": {"podcasts": drama_podcasts, },
        "Music": {"podcasts": music_podcasts, }
}
        

# add them to the dictionaries above.
# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category.
# if you are using Python 2.x then use cats.iteritems() see
# http://docs.quantifiedcode.com/python-anti-patterns/readability/
# for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["podcasts"]:
            add_podcast(c, p["title"],p["publish_date"],p["url"],p["duration"], p["RSS_feed"], p["category"],p["description"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_podcast(cat, title, publish_date, url, duration, RSS_feed, category, description):
    p = Podcast.objects.get_or_create(category=cat, title=title)[0]
    p.publish_date=publish_date
    p.url=url
    p.duration=duration
    p.RSS_feed=RSS_feed
    p.category=category
    p.description=description
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting YAPS population script...")
    populate()
