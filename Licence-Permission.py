{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNs6BvkbavE5wt9jnJKasMN"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":10,"metadata":{"id":"KL8Udtj18QoE","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1739502618542,"user_tz":-330,"elapsed":5901,"user":{"displayName":"Hardik Patel","userId":"09387059913095957585"}},"outputId":"9a3facbf-1fc0-4a1d-d645-365a298ef53c"},"outputs":[{"output_type":"stream","name":"stdout","text":["---------------------------------\n","\tLicence Manager 🪪\n","---------------------------------\n","Enter Your Age : 34\n","---------------------------------\n","You Have Licence ? Y / N : y\n","---------------------------------\n","Thank You\n","---------------------------------\n","Thanks For Using Licence Manager💐\n","---------------------------------\n","Game Designed By\n","\t ~ H a c k y B o y\n","---------------------------------\n","Developer - Hardik Patel\n"]}],"source":["print(\"---------------------------------\")\n","print(\"\\tLicence Manager 🪪\")\n","print(\"---------------------------------\")\n","a = int(input(\"Enter Your Age : \"))\n","print(\"---------------------------------\")\n","if a < 18 :\n","  print(\"You Should Wait Till 18 Then Apply For Licence\")\n","else :\n","  b = input(\"You Have Licence ? Y / N : \").strip().upper()\n","  if b == \"Y\":\n","    print(\"---------------------------------\")\n","    print(\"Thank You\")\n","  elif b == \"N\":\n","    print(\"---------------------------------\")\n","    print(\"You Have To Apply For Licence\")\n","  else:\n","    print(\"Invalid Input\")\n","\n","print(\"---------------------------------\")\n","print(\"Thanks For Using Licence Manager💐\")\n","print(\"---------------------------------\")\n","print(\"Software Designed By\\n\\t ~ H a c k y B o y\\n---------------------------------\\nDeveloper - Hardik Patel\")"]}]}