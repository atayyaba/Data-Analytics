8#import nltk
from django.shortcuts import render, render_to_response
import pandas as pd
import pandasql as ps
import pyodbc
import networkx as nx
import numpy as np
#import matplotlib.pyplot as plt

CPortal = pd.read_csv("D:\\1st semester\\Data Science\\Journal and Conference\\Journal and Conference\\ConferencePortal.csv",sep = ",")
Jportal = pd.read_csv("D:\\1st semester\\Data Science\\Journal and Conference\\Journal and Conference\\JournalPortal.csv",sep = ",")


def home(request):
    global new,newstate
    global newvalue
    z = []
    graph = []
    context = {}
    state = ""
    if request.method == 'GET':
        state = request.GET.get('search', None)
        new= request.GET.get('select', None)
        context['state'] = state
        context['new'] = new
        print(state)
    if state is not None:
        print(state)
        print(new)
        newstate=state
        search = state.strip().split(" ")
        search = [word for word in search if word not in nltk.corpus.stopwords.words('english')]
        search = search[-2:]
        search = ' '.join(search).title()
        cnxn = pyodbc.connect(
            "Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V6708T2\MSSQLSERVER01;Database=DblpXml;Trusted_Connection=yes;")
        df = pd.read_sql_query("SELECT ID FROM [DblpXml].[dbo].[Person] WHERE Name='" + state + "';", cnxn)
        print(df)
        v = df.items()
        #c = len(CPortal.ID == v)
        #print(len(Jportal.ID == v))
        #j = len(Jportal.ID == v)
        b=v
        try:
            print(len(CPortal[CPortal["ID"] == df.iloc[0,0]]))
            c = CPortal[CPortal["ID"] == df.iloc[0,0]]
            conference=c['Title'].iloc[0]
            print(len(CPortal[CPortal["ID"] == df.iloc[0,0]]))
            j = CPortal[CPortal["ID"] == df.iloc[0,0]]
            journal = j['Title'].iloc[0]
            c1=len(c)
            j1=len(j)

            if (c1 >= j1):
                newvalue="Focus of Author is towards Conferences of "+conference

            elif (c <= j1):
                newvalue="Focus of Author is towards Journal of "+journal
        except:
            newvalue="Not found"
        #showing Bar graph of conferences and journal
        objects = ('Journal', 'Conference')
        y_pos = np.arange(len(objects))
        performance = [j1, c1]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Focus of search ')

        plt.show()
        #finding Same For
        c = {}
        a = new
        df1 = CPortal[['ID', 'For', 'Title']]
        df2 = Jportal[['ID', 'For', 'Title']]
        rslt_df = df2.loc[df2['For'] == a]
        print(rslt_df)
        ID = rslt_df['ID']
        nID = ID.iloc[0]
        print(nID)
        #to check
        id = 445
        d = str(id)
        s = [str(i) for i in ID]
        for i in s:
            cnxn = pyodbc.connect(
                "Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V6708T2\MSSQLSERVER01;Database=DblpXml;Trusted_Connection=yes;")
            df = pd.read_sql_query(
                "SELECT BibliographyID FROM [DblpXml].[dbo].[PersonDetails] WHERE PersonID='" + i + "';", cnxn)
            graph.append(len(df))

        print(graph)
        for value in ID:
            c['key'] = value

        for i in graph:
            c['key'] = i
        print(c)

        data = np.mat(graph)
        rows, cols = np.where(data > 0)

        edges = zip(rows.tolist(), cols.tolist())

        G = nx.Graph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)

        nx.draw(G, pos, node_size=10, with_labels=True)
        plt.show()

        #{'state': newstate},
        return render_to_response('boards/home.html',{'form':newvalue},{'z': z})
    else:
       return render(request, 'boards/home.html')


