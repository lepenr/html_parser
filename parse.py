from bs4 import BeautifulSoup
import os

# url = 'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
# res = requests.get(url)
input_html = '{test}{test}{teste}<div class="u-privacy"><section class="u-section"><section class="u-wrapper"><div class="article-img-wrapper"><img src="/assets/images/blog/lettuce.jpg" alt="" class="article-img"></div><header><h1 class="u-heading u-heading--purple u-heading--center">The Pregnancy Boost: 4 supplements to increase your fertility</h1></header><p> Did you know that the average age of first-time mothers has risen from 25 to 29.5 in the past 20 years? And that in the past two decades, women’s issues with subfertility have increased, and now hover at an astonishing 40-50%? </p><p> As women wait longer before attempting their first pregnancy, the need to monitor and care for one’s own fertility has also risen (though fertility does not drop quite as dramatically after 30 as many blogs out there will lead you to believe). Additionally, environmental factors, recreational drinking and smoking, and external stressors can make it even more difficult to conceive. </p><p> Thankfully, today’s couples have an array of resources available to them to help them balance their hormones, improve fertility, increase sperm health and motility, and prepare the body for a successful pregnancy. </p><p> Here, we’ve compiled a list of five major supplements that our clinic can confidently recommend to improve your fertility and overall reproductive and hormonal health. </p><br><h2>1. Folic Acid</h2><p> An great supplement for a healthy diet - and an often-recommended one for women and men trying to get pregnant - is folic acid. As a major B vitamin, folic acid is instrumental in reducing the potential for neural tube defects - and congenital heart defects - in foetuses. </p><p> When you’re trying to conceive, both partners should take a folic acid supplement, in addition to whichever vitamins they are already taking daily. Additionally, ingestion of folates (folic acid in natural form) is another healthy way to boost fertility, through increasing the presence of dark, leafy greens in your diet. </p><p> Women trying to conceive should aim for .4 mg of folic acid daily. Since the sperm cycle for men takes 80 days, it is generally recommended to begin a daily dose of folic acid as soon as a couple begins trying to conceive. </p><br><h2>2. L-Arginine</h2><p> Taking L-Arginine can benefit both male and female fertility, and is often recommended for couples trying to conceive. It is instrumental in helping the body produce Nitric Oxide, which promotes blood flow to the genitalia and ovaries. </p><p> Not only is L-Arginine generally accepted as a libido booster for women, but is also used to naturally improve the sexual functioning in men, and is popularly used by men over the age of 40 as a natural alternative to Viagra. Regarding any direct effect on efforts to conceive, L-arginine is capable of increasing both the amount and motility of sperm. For women, L-Arginine can increase cervical mucus. </p><br><h2>3. Vitamin D</h2><p> Though it is often simply thought of a “sunshine vitamin,” vitamin D is widely recognized as a key component to both a successful conception and a healthy, live delivery. Maintaining an optimal Vitamin D level in the body is achievable with enough sunlight exposure. However, most men and women do not absorb enough sunlight to reach this ideal threshold annually. </p><p> Vitamin D is not commonly found in foods. A vitamin D deficiency can directly reduce female fertility and lower the healthiness of a pregnancy. Therefore, screening female patients looking to get pregnant for vitamin D levels is common practice. Some studies have shown that a normal vitamin D level increases the likelihood of Caucasian women conceiving with IVF four times more likely than those with low vitamin D levels. Black and Hispanic women are often at risk of low vitamin D levels, and should therefore take extra care to ensure their levels are conducive to pregnancy while trying to conceive. </p><p> If you’re wondering whether a vitamin D deficiency is obstructing your attempts to get pregnant, check with your physician. They will be able to recommend a supplement regime appropriate for your particular circumstances to boost your fertility and health. </p><br><h2>4. Antioxidants</h2><p> An imbalance between antioxidants and free radicals (oxygen-containing molecules with an electron imbalance) is known as oxidative stress. This bodily stress can be brought on by a number of female subfertility issues, including poor egg quality, damage to the fallopian tubes, and ovulation disorders. Combating oxidative stress in the body is an excellent way to improve fertility, and this can be achieved by increasing available antioxidants. </p><p> For both men and women, taking an antioxidant supplement can boost fertility. Partners can also increase their intake of natural antioxidants through eating antioxidant-rich foods, like blueberries, pumpkin, carrots, spinach, nuts, and teas. </p><p> Though there is no replacement for fertility treatment methods such as IVF and egg donation when they are required, female and male partners can work together to ensure that they are doing everything they can to naturally improve the health of their sperm and eggs, balance their hormones, and provide an ideal, balanced, rich environment for a developing foetus. </p></section></section></div>'

def createNeonFile(html_string):
    # html_page = input_html
    soup = BeautifulSoup(html_string, 'html.parser')
    text = soup.find_all(text=True)

    i = 0
    list_values = []
    list_attr = []
    lang_file= ''

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script'
    ]

    ignore_file = [
            " ",
            '',
            '  ',
            ' ',
            " "
        ]

    for t in text:
        if t.parent.name not in blacklist:
            i = i + 1 ; list_values.append(format(t)); list_attr.append(t.parent.name + '_' + str(i));
    #
    j=0
    for t in list_values:
        if t != " " and t !=  ")" and t !=  ' “)' and t !=  '“)':
    	    lang_file+= '\n ' + list_attr[j] + ': "' + t + '"'; j = j + 1
    return lang_file

# 

def createHtmlFile(html_string,inputRowData):
    # html_page = input_html
    soup = BeautifulSoup(html_string, 'html.parser')
    text = soup.find_all(text=True)

    i = 0
    list_values = []
    list_attr = []
    lang_file= ''

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script'
    ]

    ignore_file = [
            " ",
            '',
            '  ',
            ' ',
            " "
        ]

    for t in text:
        if t.parent.name not in blacklist:
            i = i + 1 ; list_values.append(format(t)); list_attr.append(t.parent.name + '_' + str(i));
    #
    j=0
    for t in list_values:
        if t != " " and t !=  ")" and t !=  ' “)' and t !=  '“)':
            c = inputRowData.replace(list_values[j], list_attr[j]);print(inputRowData)
    return c



# print(lang_file)


# directory = r'/Users/robert/Documents/yolk/html_parser'
# for filename in os.listdir(directory):
#     if filename.endswith(".txt"):
#         # print(os.path.join(directory, filename))
#         # print('test')
#         data=''
#         with open(os.path.join(directory, filename), 'r') as file:
#             data = file.read()
#         f = open(os.path.join(directory,'new_'+ filename),"w+")
#         f.write(createNeonFile(data))
#         f.close()
#     else:
#         continue

directory = r'/Users/robert/Documents/yolk/html_parser'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # print(os.path.join(directory, filename))
        # print('test')
        data=''
        with open(os.path.join(directory, filename), 'r') as file:
            data = file.read()
        f = open(os.path.join(directory,'neon_'+ filename),"w+")
        f.write(createHtmlFile(data,data))
        f.close()
    else:
        continue