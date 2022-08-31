from operator import index
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website import wordclouding
from website.plots import *
from .models import Thought
from . import db
import json
from .sentiment_no_voice  import thought_entry
import pandas as pd
from .frequency import word_frequency, word_frequency_pairs
import sqlite3
from .wordclouding import wordclouding
import os
from .sentiment_specialist  import *
from website import sentiment_specialist

views = Blueprint('views', __name__)

con = sqlite3.connect('website/database.db', check_same_thread=False)

cursor = con.cursor()


@views.route('/', methods=['GET', 'POST'])
@login_required
def your_thoughts():

    x = current_user.id

    query = f"SELECT * FROM Thought WHERE user_id = {x}"

    cursor.execute(query)
    result = cursor.fetchall()

    len_thoughts = len(result)
 
   

    thoughts_df = pd.DataFrame(columns = ['Thoughts','Sentiment'])

    

    if request.method == 'POST':

        thought = request.form.get('thought')
        sentiment = thought_entry(thought)

       
       

        if len(thought) < 1:
            flash('Thought is too short!', category='error')
        else:
            new_thought = Thought(data=thought, user_id=current_user.id, sentiment_class = sentiment)
            db.session.add(new_thought)
            db.session.commit()
            flash('Thought added!', category='success')
            thoughts_df.loc[len(thoughts_df.index)] = [thought, sentiment]
            #entry = Thought.query.filter_by(user_id = current_user.id, sentiment_class = sentiment)
            entry = Thought.query.filter_by(user_id = current_user.id, sentiment_class = sentiment).order_by(Thought.id.desc()).first()
            
        
      
            

        return render_template("your_thoughts.html", user = current_user, titles=thoughts_df.columns.values, entry = entry, len_thoughts = len_thoughts) # thought = thought basically 
                                                                                                                                # means that we can use that variable
                                                                                                                   # on our your_thoughts.html with jinga

    else:
        entry = Thought.query.filter_by(user_id = current_user.id).all()
        return render_template("your_thoughts.html", user = current_user, entry = entry, len_thoughts = len_thoughts)




@views.route('/your-mind', methods=['GET', 'POST'])
@login_required
def your_mind():

    print(current_user.id)
    print(type(current_user.id))

    query = "SELECT * FROM Thought WHERE user_id = ?"

    item = current_user.id

    cursor.execute(query, [item])    

    result = cursor.fetchall()

    text = " ".join([i[1] for i in result])

    word_freq = word_frequency(text) # the table -> to delele from the HTML

    word_pairs = word_frequency_pairs(text)


    try:

        word_cloud = wordclouding(word_freq) ## render image ?
        freq_plot = plotting_frequency(word_pairs)

    except:
        print("An exception occurred")

    return render_template("your_mind.html",user = current_user, tables=[word_freq.to_html(classes='data')], titles=word_freq.columns.values)



@views.route('/meditation', methods=['GET', 'POST'])
@login_required
def meditation():

    return render_template("meditation.html", user=current_user)



@views.route('/your-mind-athletes', methods=['GET', 'POST'])
@login_required
def your_patients():

    thought_entries_df = pd.DataFrame(columns = ['Thoughts','Sent_Negative','Sent_Neutral','Sent_Positive',
                                                'Sentiment','Timestamp'])
    

    if request.method == 'GET':
        queryid = "SELECT id, first_name FROM USER WHERE role = 'User'"

        cursor.execute(queryid)
        result = cursor.fetchall()


        userdf = pd.DataFrame(result, columns=['id', 'name'])


        return render_template("your_patients.html", user=current_user,userdf=userdf)

    elif request.method == 'POST':

        x = request.form.get('userbutton') 

        query = f"SELECT * FROM Thought WHERE user_id = {x}"

        cursor.execute(query)

        result = cursor.fetchall()

        thoughts_specialist = pd.DataFrame(result, columns = ['index','Thought','Timestamp','user_id','Sentiment'])

        thoughts_specialist = thoughts_specialist.drop(['index','user_id'], axis = 1)

        queryid = f"SELECT first_name FROM USER WHERE id = {x}"

        cursor.execute(queryid)

        result = cursor.fetchall()

        user_name = result[0][0]



        #text = " ".join([i[1] for i in result])

        # word_freq = word_frequency(text)

        #for i, j in pd.Series(result).iteritems():
         #   thought_entry_specialist(str(j))

        # thought_entries_df.loc[len(thought_entries_df.index)] = thought_entry_specialist('what is this')

        sent_scores = thoughts_specialist[:50].apply(spec_apply, axis = 1)

        sent_scores = pd.DataFrame.from_dict(dict(zip(sent_scores.index, sent_scores.values))).transpose()

        try:
            sent_scores.columns = ['Negative', 'Neutral', 'Positive']
            plot_spec(sent_scores.index,sent_scores['Positive'])


        except:
            print('Something has happened')


        return render_template("your_patients_post.html",user = current_user, tables=[thoughts_specialist.tail(10).sort_index(axis = 0, ascending = False).to_html(classes='data',index=False)], titles=thoughts_specialist.columns.values, zip = zip, user_name = user_name)

