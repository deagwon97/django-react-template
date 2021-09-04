import 'react-perfect-scrollbar/dist/css/styles.css';
import { useRoutes } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/core';
import GlobalStyles from 'src/components/GlobalStyles';
import 'src/mixins/chartjs';
import theme from 'src/theme';
import routes from 'src/routes';

export const BACKEND_API = 'http://localhost:8000/api';
// export const DJANGO_API_SERVER =
//   NODE_ENV === 'development'
//     ? process.env.REACT_APP_DJANGO_API_SERVER
//     : window.DJANGO_API_SERVER;
console.log('#########', BACKEND_API);

const App = () => {
  const routing = useRoutes(routes);

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />
      {routing}
    </ThemeProvider>
  );
};

export default App;
