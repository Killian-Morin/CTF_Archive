# "J'ai faim" he said

## Clue / Information

A famous and wealthy explorer owns a time machine. He uses it to move forward in time to November 2024. He dines near the Mechanical Monument, a masterpiece by engineers Richard Rogers and Renzo Piano. He orders a Menu for €17.90 and a ""Café Gourmand"" on a Saturday at 3 a.m. How much did he pay in total?

Provide the MD5 hash of the total amount rounded to the nearest whole number.

Example: 15.4 <=> 15 -> 9bf31c7ff062936a96d3c8bd1f8f2ff3

Flag format: HACKDAY{md5}

## Resolution

The Pompidou Museum was designed by Richard Rogers and Renzo Piano.

On Google Maps, select _Restaurant_, hours: open a Saturday at 3 A.M
the first result is Chouchou, check the [menu](https://restaurantchouchouparis.fr/menu),
the "Café Gourmand" is at €10.90 and the Menu is indeed for €17.90 but _Extrachange + 2.50 evening, week-end and public holidays - Drink not included_.

10.90 + 17.90 + 2.50 = 31.3 <=> 31 -> c16a5320fa475530d9583c34fd356ef5 but it's not that

Let's try without the +2.5

31.1 - 2.5 = 28.8 <=> 29 -> c81e728d9d4c2f636f067f89cc14862c not that either

There is also a note about the Hot Beverages:
_from 5pm, hot drinks are subject to a +0.7 surcharge_

So the final addition is: 10.90 + 0.7 + 17.90 + 2.50 = 32 <=> 6364d3f0f495b6ab9dcf8d3b5c6e0b01

Attempted flags:
- `HACKDAY{c16a5320fa475530d9583c34fd356ef5}`
- `HACKDAY{c81e728d9d4c2f636f067f89cc14862c}`
- `HACKDAY{6364d3f0f495b6ab9dcf8d3b5c6e0b01}` -> correct flag

### author => [@komorebi](https://github.com/Killian-Morin)
