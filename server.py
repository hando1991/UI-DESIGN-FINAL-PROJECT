from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
current_id = 10

data = {
    "1":{
        "id":"1",
        "name": "Receivables",
        "property":["The sales a business has made.","The amount of money received for goods or services.","The amount of money owed at the end of each month varies (debtors)."],
        "image":"https://cdn.wallstreetmojo.com/wp-content/uploads/2019/07/Accounts-Receivable-Examples.jpg",
        "summary":"Accounts receivable, abbreviated as AR or A/R,are legally enforceable claims for payment held by a business for goods supplied or services rendered that customers have ordered but not paid for. These are generally in the form of invoices raised by a business and delivered to the customer for payment within an agreed time frame. Accounts receivable is shown in a balance sheet as an asset. It is one of a series of accounting transactions dealing with the billing of a customer for goods and services that the customer has ordered. These may be distinguished from notes receivable, which are debts created through formal legal instruments called promissory notes."

    },
    "2":{
        "id":"2",
        "name": "Inventory",
        "property":["Inventory is the raw materials used to produce goods as well as the goods that are available for sale.","It is classified as a current asset on a company's balance sheet.","The three types of inventory include raw materials, work-in-progress, and finished goods. ","Inventory is valued in one of three ways, including the first-in, first-out method; the last-in, first-out method; and the weighted average method."],
        "image":"https://assets-global.website-files.com/600fe6e1ff56087409a9f096/602b9f28bb288a2b7eea1217_Inventory-Reduction-Strategies-For-Excess-Or-Slow-Moving-Stock.jpg",
        "summary":"The term inventory refers to the raw materials used in production as well as the goods produced that are available for sale. A company's inventory represents one of the most important assets it has because the turnover of inventory represents one of the primary sources of revenue generation and subsequent earnings for the company's shareholders. There are three types of inventory, including raw materials, work-in-progress, and finished goods. It is categorized as a current asset on a company's balance sheet."
    },
    "3":{
        "id":"3",
        "name": "Property Plant and Equipment",
        "property":["Property, plant, and equipment (PP&E) are long-term assets vital to business operations and the long-term financial health of a company.","Equipment, machinery, buildings, and vehicles are all types of PP&E assets."," (PP&E) are also called fixed or tangible assets, meaning they are physical items that a company cannot easily liquidate."],
        "image":"https://accountingplay.com/wp-content/uploads/2015/08/H_10F_Property_plant_and-equipment.png",
        "summary":"Property, plant, and equipment (PP&E) are long-term assets vital to business operations. Property, plant, and equipment are tangible assets, meaning they are physical in nature or can be touched; as a result, they are not easily converted into cash. The overall value of a company's PP&E can range from very low to extremely high compared to its total assets."
    }
}

quizData = {
    "1":{
        "id":"1",
        "description" : "What part of the balance sheet should this entry be in?",
        "image": "https://preview.redd.it/odlpqr5rb6u81.png?width=536&format=png&auto=webp&s=4711797c9a29e67102d013ed0c4e90c44b5ee963",
        "entry1": "A.Assets",
        "entry2": "B.Liabilities",
        "entry3": "C.Equity",
        "correct": "A",
    },  
    "2":{
        "id":"2",
        "description" : "Which of the following is not a typical entry in asset ?",
        "image": "",
        "entry1": "A. Inventory",
        "entry2": "B. Earning Per Share",
        "entry3": "C. Property Plant and Equipment",
        "correct": "B",
    },
    "3":{
        "id":"3",
        "description" : "Which of the following is not a typical entry in liabilities ?",
        "image": "",
        "entry1": "A. Deferred revenue",
        "entry2": "B. Long-term debt",
        "entry3": "C. Property Plant and Equipment",
        "correct": "C",
    },
    "4":{
        "id":"4",
        "description" : "What is the total assets if total liabilities = $10000 and total equity = $5000 ?",
        "image": "",
        "entry1": "A. 5000",
        "entry2": "B. 10000",
        "entry3": "C. 15000",
        "correct": "C",
    },
    "5":{
        "id":"5",
        "description" : "What is the total liabilities if total asset = $10000 and total equity = $5000 ?",
        "image": "",
        "entry1": "A. 5000",
        "entry2": "B. 10000",
        "entry3": "C. 15000",
        "correct": "A",
    }
}

options=[];

# ROUTES
@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/learn1/',methods=['GET', 'POST'])
def learn1():
    return render_template('entry.html')


@app.route('/view/<id>')
def view(id=None):
    movie_name = ""
    # show the user profile for that user
    for key in data.keys():
        if id==key:
            input_data = data[id]
    return render_template('view.html',input_data=input_data,data = data)



@app.route('/quiz/<id>')
def quiz(id=None):
    if int(id)==1:
        del options[:]
    return render_template('quiz.html',questionId=id,questionRes=False)


@app.route('/question/<id>')
def question(id=None):
    for key in quizData.keys():
        if id==key:
            input_data = quizData[id]
    return jsonify(input_data)


@app.route('/question',methods=["POST"])
def questionSubmit():
    options.append(request.get_json())
    return jsonify(options)

@app.route('/res')
def res(id=None):
    return render_template('res.html')

@app.route('/resData')
def resData(id=None):
    return jsonify(options)

@app.route('/reslart')
def reslart(id=None):
    del options[:]
    return jsonify(options)

@app.route('/quiz/res/<id>')
def quizRes(id=None):
    return render_template('quiz.html',questionId=id,questionRes=True)

@app.route('/question/res/<id>')
def questionRes(id=None):
    return jsonify(options[int(id)-1])


if __name__ == '__main__':
   app.run(debug = True)





