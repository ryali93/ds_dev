from django.shortcuts import render, redirect
from django.http import HttpResponse

import pandas as pd
import docx
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Document
from .forms import DocumentForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def process_cv(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = DocumentForm()

    return render(request, 'process_cv.html', {
        'form': form
    })


def list_cv(request):
    df = pd.DataFrame(list(Document.objects.all().values()))
    df = df [['id', 'document', 'uploaded_at']]
    df.id = df.id.astype(str)

    def add_url(data):
        output = "<a href = '{}'>{}</a>".format(data, data)
        return output

    df.id = df.id.apply(add_url)

    html_table = df.to_html(
        escape=False,
        index=False,
        border=1,
        classes = "table table-striped table-hover",
        )
    params = {'html_table': html_table}
    return render(request, 'list_cv.html', params)

def read_word(filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        out = '\n'.join(fullText)
        return out

def jobmatrix():
    job_raw = pd.read_excel("bumeran.xlsx", encoding='cp1252')
    desc = job_raw.DESCRIPCION
    puesto = job_raw.PUESTO
    url = job_raw.URL
    def desc_to_words(raw):
        letras = re.sub("[^a-zA-ZáéíóúñÑ]", " ", raw)
        words = letras.lower().split()
        stops = set(stopwords.words('spanish'))
        meaningfull_words = [w for w in words if not w in stops]
        return (" ".join(meaningfull_words))
    desc_limpio = []
    num_filas = desc.size
    for i in range(0, num_filas):
        desc_limpio.append(desc_to_words(desc[i]))
    desc_limpio = pd.Series(desc_limpio)
    global tfidf_vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    jobmatrix = tfidf_vectorizer.fit_transform(desc_limpio)
    return jobmatrix, puesto, url

def cvmatrix(wordout):
    letrascv = re.sub("[^a-zA-ZáéíóúñÑ]", " ", wordout)
    minusculascv = letrascv.lower()
    palabrascv = minusculascv.split()
    palabrascv = [w for w in palabrascv if not w in stopwords.words("spanish")]
    resultadocv = " ". join(palabrascv)
    desc_limpio_cv = pd.Series(resultadocv)
    cvmatrix = tfidf_vectorizer.transform(desc_limpio_cv)
    return cvmatrix

def cv_specific(request, cv_id):

    filename = Document.objects.values_list('document', flat=True).get(id=cv_id)
    wordout = read_word(filename)
    jobmat = jobmatrix()
    cvmat = cvmatrix(wordout)
    res = cosine_similarity(cvmat, jobmat[0], True)
    res = res[0]
    size = len(res)
    job_simil = pd.DataFrame(columns=('ID', 'Puesto', 'URL', 'Similitud'))
    i = int()
    for i in range(0, size):
        job_simil.loc[i] = [i+1, jobmat[1][i], jobmat[2][i], res[i]]
    sorted_job = job_simil.sort_values(['Similitud'], ascending=False)
    print(sorted_job)
    html_match = sorted_job.to_html(
        formatters = {
        'Similitud': '{:,.2%}'.format
        },
        index = False,
        border = 1,
        classes = "table table-striped table-hover",
        escape = False
        )
    params = {'html_match': html_match}
    return render(request, 'match.html', params)






