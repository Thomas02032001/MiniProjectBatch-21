import './App.css';
import NewsList from './components/NewsList';
import './components/NewsItem.css'
function App() {
  return (
    <div className="App">
      <div className="heading">
        <h3 className="h3heading">COVID UPDATES</h3>
      </div>
      <NewsList/>    
    </div>
  );
}

export default App;
