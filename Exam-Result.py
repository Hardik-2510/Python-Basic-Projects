{"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"background_save":true,"base_uri":"https://localhost:8080/"},"id":"-NpmdNwvV5oa"},"outputs":[{"name":"stdout","output_type":"stream","text":["\n","═════════════════════════════════════════════\n","        🎓 STUDENT DETAILS ENTRY 📜       \n","═════════════════════════════════════════════\n"]}],"source":["# Exam Result Analysis\n","import time\n","import os\n","\n","sub1 = sub2 = sub3 = sub4 = sub5 = total = obtain = per = 0\n","s_name = \"\"\n","enroll = 0\n","grade = \"\"\n","\n","def getting_details():\n","    global s_name, enroll, sub1, sub2, sub3, sub4, sub5\n","\n","    os.system('cls')\n","\n","    print(\"\\n\" + \"═\" * 45)\n","    print(\"        🎓 STUDENT DETAILS ENTRY 📜       \")\n","    print(\"═\" * 45)\n","\n","    s_name = input(\"👤 Enter Student Name : \").strip()\n","\n","    enroll = input(\"🆔 Enter Enrollment Number : \")\n","    while not enroll.isdigit():\n","        print(\"❌ Invalid input! Please enter a numeric enrollment number.\")\n","        enroll = input(\"🆔 Enter Enrollment Number : \")\n","    enroll = int(enroll)\n","\n","    print(\"\\n\" + \"═\" * 45)\n","    print(\"📢 Note: Enter Marks Out of 60\")\n","    print(\"═\" * 45)\n","\n","    sub1 = int(input(\"Enter OOPJ Marks :\"))\n","    sub2 = int(input(\"Enter DBMS Marks :\"))\n","    sub3 = int(input(\"Enter DS Marks :\"))\n","    sub4 = int(input(\"Enter DLD Marks :\"))\n","    sub5 = int(input(\"Enter EM-3 Marks :\"))\n","    return sub1 , sub2 , sub3 , sub4 , sub5 , s_name , enroll\n","\n","def calculate():\n","    global total, obtain, per\n","    total = 300\n","    obtain = sub1 + sub2 + sub3 + sub4 + sub5\n","    per = (obtain/300)*100\n","\n","    return per , obtain , total\n","\n","def waiting():\n","    if sub1 \u003c= 60 and sub2 \u003c= 60 and sub3 \u003c= 60 and sub4 \u003c= 60 and sub5 \u003c= 60:\n","      i = 10\n","      while i \u003e 0 :\n","        if i % 2 == 1 :\n","            os.system('cls')\n","            print(f\"⏰ Wait {int(i/2)} Sec... ⏰\")\n","            time.sleep(2)\n","            i-=1\n","        else :\n","            os.system('cls')\n","            print(f\"📃 We're Generating Result... 📃\")\n","            time.sleep(2)\n","            i-=1\n","        calculate()\n","    else :\n","        os.system('cls')\n","        print('Invalid Marks ❌!!')\n","        exit()\n","\n","def grading():\n","    global grade\n","    if per \u003e= 85 and  per \u003c= 100 :\n","        grade = \"A\"\n","    elif per \u003e= 75 and per \u003c= 85 :\n","        grade = \"B\"\n","    elif per \u003e= 65 and per \u003c= 75 :\n","        grade = \"C\"\n","    elif per \u003e= 50 and per \u003c= 65 :\n","        grade = \"D\"\n","    elif per \u003e= 35 and per \u003c= 50 :\n","        grade = \"P\"\n","    else :\n","        grade = \"F\"\n","    return grade\n","\n","def print_result():\n","    global total, obtain, per, grade\n","    os.system('cls' if os.name == 'nt' else 'clear')\n","\n","    print(\"\\n\" + \"═\" * 45)\n","    print(\"        🎓 UKA TARSADIA UNIVERSITY 🎓       \")\n","    print(\"          📜 SEMESTER-3 RESULT 📜           \")\n","    print(\"═\" * 45)\n","\n","    print(f\"👤 Student Name : {s_name}\")\n","    print(f\"🆔 Enrollment   : {enroll}\")\n","    print(\"═\" * 45)\n","\n","    print(f\"{'📚 Subject':\u003c15}{'🔢 Total':\u003c10}{'📝 Obtained':\u003c10}\")\n","    print(\"─\" * 45)\n","\n","    print(f\"🪪  OOPJ       |   60     |   {sub1:\u003e2}  \")\n","    print(f\"💾 DBMS       |   60     |   {sub2:\u003e2}  \")\n","    print(f\"📊 DS         |   60     |   {sub3:\u003e2}  \")\n","    print(f\"⚡ DLD        |   60     |   {sub4:\u003e2}  \")\n","    print(f\"📏 EM-3       |   60     |   {sub5:\u003e2}  \")\n","    print(\"─\" * 45)\n","\n","    print(f\"📈 TOTAL      |  {total}    |  {obtain}  \")\n","    print(\"─\" * 45)\n","    print(f\"🎯 Percentage : {per:.2f}% out of 100%\")\n","    print(\"═\" * 45)\n","\n","    if grade == \"F\":\n","        print(f\"❌ Grade : {grade} | *Sorry, You Failed! 😞\")\n","    else:\n","        print(f\"🏆 Grade : {grade}   | 🎉 Congratulations! 🎉\")\n","    print(\"═\" * 45)\n","\n","def dev():\n","    print(\"                ~  Dev Info  ~        \")\n","    print(\"─\" * 45)\n","    print(\"🎨 Software Designed By\\n\\t         ~ H a c k y B o y\")\n","    print(\"─\" * 45)\n","    print(\"           💻 Developer - Hardik Patel\")\n","    print(\"═\" * 45)\n","\n","getting_details()\n","calculate()\n","grading()\n","waiting()\n","print_result()\n","dev()"]}],"metadata":{"colab":{"authorship_tag":"ABX9TyOiUAsIDpgJDG4hkLifFgW8","name":"","version":""},"kernelspec":{"display_name":"Python 3","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":0}