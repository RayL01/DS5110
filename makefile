

.PHONY: data, clean

answer: data/2020RES_APR2019PubDataShare.csv
		python -B src/main.py


data/2020RES_APR2019PubDataShare.csv:
		mkdir -p data
		cd data; curl -LO https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv
clean:
		rm data/2020RES_APR2019PubDataShare.tsv