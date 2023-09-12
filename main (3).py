#2.2 Implement a class called Player that represents a cricket player.The Player cvlass should have a method called play() which prints"The player is playing cricket.Derive two classes,Batsman and Bowler,from the Player class.Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling",respectivly.Write a program to create objects of both the Batsman and Bowler classes asnd call the play() method for each object.
#Define the player class
class Player:
  def play(self):
    print("the player is playing cricket.")
    #Define the Batman class,derived from player
    class Batsman(Player):
      def play(self):
        print("The batsman is batting.")
    #define the Bowler class,derived from player
    class Bowler(Player):
      def play(self):
        print("The bowler is bowling.")
    #create objects of Batsman and Bowler classes
    batsman = Batsman()
    bowler = Bowler()
    #call the play()method for each object
    batsman.play()
    bowler.play()


