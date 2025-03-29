import sys
from flask import Blueprint, request
from transformers import BertJapaneseTokenizer, BertForTokenClassification
from transformers import pipeline
import json

api = Blueprint(
	"api",
	__name__,
)

@api.route("/")
def index():

	#text = "国内の乗用車メーカー8社が28日にまとめた2025年2月の輸出台数で、マツダや三菱自動車の対北米輸出が前年同月から増えた。両社ともトランプ米政権による関税発動を見据えた動きではないとした。マツダや三菱自は米国販売の大半を日本から輸出しており、関税発動前の3月に輸出を増やす可能性もある。"
	#text = "三井住友海上火災保険とあいおいニッセイ同和損害保険が2027年4月をめどに合併する方針を決めた。10年4月の経営統合で両社を束ねる持ち株会社のMS&ADインシュアランスグループホールディングスが発足したものの、強みや顧客基盤の違いを理由に併存を続けてきた。結成から15年となるMS&ADグループは大きな節目を迎える。"

	# http://127.0.0.1:5000/api/?q=に続くクエリ文字列を取得してtextに代入
	text = ""
	if request.args.get("q") is not None:
		text = request.args.get("q")
	else:
		text ="No Text"

	# モデルの読み込み
	model = BertForTokenClassification.from_pretrained("jurabi/bert-ner-japanese")
	# トークナイザーの読み込み
	tokenizer = BertJapaneseTokenizer.from_pretrained("jurabi/bert-ner-japanese")
	# パイプラインの設定
	ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)
	outputs = ner_pipeline(text)
	print(outputs)

	# entityが「B-法人名」もしくは「I-法人名」のワードを抽出してnames_tokens配列に格納
	names_tokens = []
	for output in outputs:
		if output['entity'] == 'B-法人名' or output['entity'] == 'I-法人名':
			names_tokens.append(output['word'])
		else:
			continue
	
	print(names_tokens)

	# entityが「B-法人名」の後に続く「I-法人名」をentityに持つ単語を結合し、固有名詞として配列resultsに格納
	results = []
	for i in range(len(outputs)):
		if(outputs[i]['entity'] == 'B-法人名'):
			name = outputs[i]['word']
			for j in range(i+1, len(outputs)):
				if outputs[j]['entity'] == 'I-法人名':
					name += outputs[j]['word']
				else:
					break
			results.append(name)

	# resultsをjson形式で返す
	return json.dumps(results, ensure_ascii=False)