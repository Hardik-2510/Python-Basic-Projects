{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNZilvq0t+nFGVenZgxz91x"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"BbdbzCCOFSSV","outputId":"56296c4d-d4a0-4005-eb8a-c9e43b56377b"},"outputs":[{"output_type":"stream","name":"stdout","text":["-----------------------------\n"]}],"source":["import random\n","'''\n","REFERING\n","  game_options = { 1 : \"🪨\" ,\n","                  2 : \"📃\" ,\n","                  3 : \"✂️\" }\n","'''\n","game_move = [\"🪨\" , \"📃\" ,\"✂️\"]\n","game_options = [1,2,3]\n","\n","print(\"-----------------------------\")\n","user_input = int(input(\"Welcome To 🪨 📃 ✂️ Game\\n-----------------------------\\n1. Stone(🪨)\\n2. Paper(📃)\\n3. Scissor(✂️)\\nChoose Any One By Number : \"))\n","pc = random.choice(game_options)\n","print(\"-----------------------------\")\n","print(\"PC CHOOSE :\",game_move[pc - 1])\n","print(\"USER CHOOSE :\",game_move[user_input - 1])\n","print(\"-----------------------------\")\n","if pc == user_input:\n","  print(\" Match Tie 😑\")\n","elif pc == 1 and user_input == 2:\n","  print(\" You Win 💐\")\n","elif pc == 1 and user_input == 3:\n","  print(\" You Lose 😢\")\n","elif pc == 2 and user_input == 1:\n","  print(\" You Lose 😢\")\n","elif pc == 2 and user_input == 3:\n","  print(\" You Win 💐\")\n","elif pc == 3 and user_input == 1:\n","  print(\" You Win 💐\")\n","elif pc == 3 and user_input == 2:\n","  print(\" You Lose 😢\")\n","else:\n","  print(\" Invalid Input \")\n","\n","print(\"-----------------------------\")\n","print(\"Thanks For Playing 😀\\nHope You Enjoy The Game !\")\n","print(\"-----------------------------\")\n","print(\"Game Designed By\\n\\t ~ H a c k y B o y\\n-----------------------------\\nDeveloper - Hardik Patel\")"]}]}