#include <iostream>

using namespace std;

class Human
{
public:
    Human(int SpawnAge)
    {
        Age = SpawnAge;

    }
    void Think ()
    {
        cout << GetThinkMessage() << endl;
    }

    int Age;
private:

    int SocialLevel;
    int Inteligence;
    int Luck;

    string GetThinkMessage()
    {
        if (SocialLevel + Luck > 100)
        {
            return "Estoy teniendo pensamientos felices:D" ;
        }
        else if (Luck > Inteligence)
        {
            return "Soy un suertudo";
        }
        else if (Age > 18)
        {
            return "Soy un bebe";
        }
        else
        {
            return "No pienso nada";
        }
    }

};


int main ()
{
    Human Bob (19);

    Bob.Think();

    return 0;
}
