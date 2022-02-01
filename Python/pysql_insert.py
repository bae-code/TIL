movie_list = []

#셀레니움에서 이미지 크롤링에 사용하기위한 제목리스트
title_list = []

#movie_id로 사용할 값
movie_id= 1

# db와 연결 하는 부분
conn = pymysql.connect(host= host, user = username, passwd= password, db= database, port= port, use_unicode= True, charset= 'utf8')
cursor = conn.cursor()

# 저장할 형식
sql = "INSERT INTO movies (movieid, title, openDt, clip, star, genre) VALUES (%s, %s, %s, %s, %s, %s )"


# 90년도부터 07년도 까지 연도별 100개씩 출력
for i in range(1990,2007):

    # 영화 진흥회 api
    url =f'https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&openStartDt={i}&openEndDt={i}&itemPerPage=100'
    
    res = requests.get(url)
    text = res.text

    d = json.loads(text)

    # 100개의 영화에서 제목, 장르, 개봉일, movie_id를 저장
    for i in d['movieListResult']['movieList']:
        # 제목의 공백을 지워줌
        b = i['movieNm'].replace(' ','')
        #제목의 특수문자를 지워줌
        title = ''.join(filter(str.isalnum, b))

		#장르
        genre =i['repGenreNm']
        
        # 장르를 숫자로 저장하기위한 리스트
        genre_idx=['가족','공포(호러)','다큐멘터리','드라마','멜로/로맨스','뮤지컬','미스터리','범죄','사극','서부극(웨스턴)','성인물(에로)','스릴러','애니메이션','액션','어드벤처','전쟁','코미디','판타지','SF','']
        
        #장르 index값 ex)0,12,4
        genre_int = genre_idx.index(genre)
        
        #연도만 저장함 ex ) 1994
        openDt = int(i['openDt'][:4])
		
        # 무비id(없어도될듯한데;), 타이틀, 개봉일자, 클립, 평점 평균, 장르 
        movie_list.append((movie_id,title,openDt,'',0.0,genre_int))

        #제목만 제목리스트에 따로저장
        title_list.append(title)
        #movie_id 에 +1하여 반복할수있게 함 
        
        
                
        movie_id+=1

### 저장하는 부분

retro_rds = conn.cursor()

#리스트안에 있는 모든튜플을 sql < 에 형식과 동일하게 저장함
retro_rds.executemany(sql, movie_list)

conn.commit()
