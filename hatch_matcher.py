# -----------------------------------------+
# Brendan Smith                            |  |
# -----------------------------------------|
# This program helps beginner fly          |
# fisherman identify dry flies and match   |
# the hatch.                               |
# -----------------------------------------+

import webbrowser

# Opens a new tab, if possible.
new = 2

# Opens a public URL in webbrowser to help give user fly suggestions
# along with advice on how to properly imitate that type of insect.

terristrial_url = "http://www.orvis.com/s/secrets-of-fishing-terrestrial-flies/364"
caddis_url = "http://1source.basspro.com/index.php/component/k2/67-fly-fishing/1099-fly-fishing-with-caddis"
stonefly_url = "https://tetonvalleylodge.com/stone-flies-make-sure-you-catch-the-hatch/"
midge_url = "http://www.onlinefishinglog.com/blog/22/River-Midge-Fishing-Tactics---Part-2"
mayfly_url = "http://english-fly-fishing-flies.s3-website-eu-west-1.amazonaws.com/dry-adams.html"

# Asks the user specific questions about the insect until the insect is identified,
# from there a fly is suggested in order to match the hatch along
# with an article that goes in to more detail.

question_1 = input("Is the insect hatching or coming from shore? ")
id_statement = ("You are most likley seeing a(n)")

if (question_1 == "coming from shore"):
    print(id_statement,
          "terrestrial then.. Read this article to learn more about terrestrials and how to fish them. I recommend using a Quick Size Beattle. ")
    webbrowser.open(terristrial_url, new=new)
else:
    tail = input("Does it have a tail? ")

    if (tail == "no"):
        print(id_statement,
              "caddis then.. I recommend using an Elk Haired Caddis. Here's more helpful information about the caddis fly. ")
        webbrowser.open(caddis_url, new=new)
    else:
        two_wings = input("Does it have two pairs of wings? ")

        if (two_wings == "yes"):
            print(id_statement,
                  "stonefly then.. I recommend using an orange Stimulator fly or one from the website that most resembles the fly you see. Read this article if you would like to learn more about stoneflies. ")
            webbrowser.open(stonefly_url, new=new)
        else:
            mosquito = input("Is it mosquito size or smaller? ")

            if (mosquito == "yes"):
                print(id_statement,
                      "midge then.. These are tiny and often hard to see. They sometimes can be frustrating to imitate so I recommend putting a bigger dry fly in front, such as a Stimulator with a Griffith's Gnat trailing 18 inches behind it. ")
                webbrowser.open(midge_url, new=new)
            else:
                print(id_statement,
                      "mayfly then.. I recommend using the most popular dry fly, the Adams. Read this article for more information about mayflies. ")
                webbrowser.open(mayfly_url, new=new)