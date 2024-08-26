data Str = H | E | L | O | W | R | D | Space deriving Show

helloWorld :: [Str]
helloWorld = [H, E, L, L, O, Space, W, O, R, L, D]

characterToString :: Str -> String
characterToString H = "H"
characterToString E = "E"
characterToString L = "L"
characterToString O = "O"
characterToString W = "W"
characterToString R = "R"
characterToString D = "D"
characterToString Space = " "

listToString :: [Str] -> String
listToString [] = ""
listToString (x:xs) = characterToString x ++ listToString xs

main :: IO ()
main = putStrLn (listToString helloWorld)