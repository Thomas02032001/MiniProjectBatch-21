import React, {useState, useEffect} from 'react'
import Axios from 'axios';
import NewsItem from './NewsItem';
import './NewsItem.css'
const NewsList = () => {
    const [articles, setArticles] = useState([]);
    useEffect(()=>{
        const getArticles = async()=>{
            const res = await Axios.get("https://newsapi.org/v2/everything?q=coronavirus&sortBy=publishedAt&apiKey=793d388cf40243f2a0e2c02d3703fcdb");
            // const res = await Axios.get("https://newsapi.org/v2/everything?q=tesla&from=2021-10-24&sortBy=publishedAt&apiKey=793d388cf40243f2a0e2c02d3703fcdb");
            setArticles(res.data.articles);
            console.log(res);
        };
        getArticles(); 
    },[])
    return (
        <div className="total_data">
            {
                articles.map(({title, description, url, urlToImage})=>(
                    <NewsItem title={title} description={description} url={url} urlToImage={urlToImage} />
                ))
            }
        </div>
    )
}

export default NewsList
