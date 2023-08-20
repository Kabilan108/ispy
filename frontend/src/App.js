import React, { useState } from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import ProTip from './ProTip';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import CircularProgress from '@mui/material/CircularProgress';


function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

function BoxComponent() {
  return (
    <Box component="span" sx={{ p: 2, border: '1px dashed grey' }}>
      <Button>Save</Button>
    </Box>
  );
}

function App() {
  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Material UI Create React App example
        </Typography>
        <ProTip />
        <Copyright />
      </Box>

      <BoxComponent/>
    </Container>
  );
}

// export default App;

function JokeComponent() {
  const [joke, setJoke] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchJoke = async () => {
      setLoading(true);
      try {
          const response = await fetch('http://127.0.0.1:4000/kaboom');
          const data = await response.json();
          
          if (data.success && data.data && data.data.joke) {
              setJoke(data.data.joke);
          } else {
              setJoke('Error fetching joke');
          }
      } catch (error) {
          setJoke('Error fetching joke');
      } finally {
          setLoading(false);
      }
  };

  return (
      <div>
          <Button variant="contained" color="primary" onClick={fetchJoke}>
              Tell me a joke
          </Button>
          <Box mt={2}>
              <TextField
                  fullWidth
                  multiline
                  rows={4}
                  variant="outlined"
                  value={loading ? '' : joke}
                  InputProps={{
                      readOnly: true,
                      startAdornment: loading ? <CircularProgress size={20} /> : null
                  }}
              />
          </Box>
      </div>
  );
}

export default JokeComponent;
