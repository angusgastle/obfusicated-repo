// Inform
// Inform is a design system for interactive fiction based on natural language as well as a programming language. 
// The syntax is reminiscent of a storytelling approach, making it both a narrative and computational paradigm.

Constant Story "HELLO WORLD COMPLEX";
Constant Headline "^An Interactive Fiction Story^";

Include "Parser";
Include "VerbLib";

[ Initialise;
  location = StartRoom;
];

Object StartRoom "A Mysterious Room"
  with description "You are in a room with an aura of untold stories. The room seems to have something to say...",
  has light;

Object -> Computer "old computer"
  with name 'computer' 'terminal' 'device',
       description "This ancient device seems to be from another era. Oh, it is still working!",
       before [;
         SwitchOn, TurnOn:
             StartRoom has light;
             print "The screen lights up and displays a message!^";
             rtrue;
         Examine:
             if (self hasnt light) {
                 print "The computer is off. Maybe you can turn it on.^";
             } else {
                 print_ret "The screen displays: 'Hello, World!'^";
             }
          ],
  has static;

Object LibraryActions "Action Relations"
  with description "Various actions at your command...",
  has proper;

[ SwitchOnSub;
  ! the player tries to switch something on
  if (noun has light) { "It's already on."; }
  give noun light;
  "You switch on ", (the) noun, ".";
];

[ TurnOnSub;
  ! the player tries to turn something on
  <<SwitchOn noun>>;
];

Verb 'switch' * 'on' -> SwitchOn;
Verb 'turn' * 'on' -> TurnOn;
Verb 'examine' 'x' * noun -> Examine;

[ Main;
  ! The entry point of the interactive fiction game
  Initialise();
];

Include "Grammar";