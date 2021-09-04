import { Helmet } from 'react-helmet';
import { Box, Container } from '@material-ui/core';
import InferenceListToolbar from 'src/components/inference/InferenceListToolbar';
import InferenceListResults from 'src/components/inference/InferenceListResults';
import inferences from 'src/__mocks__/inferences';

const InferenceList = () => (
  <>
    <Helmet>
      <title>Inferences</title>
    </Helmet>
    <Box
      sx={{
        backgroundColor: 'background.default',
        minHeight: '100%',
        py: 3
      }}
    >
      <Container maxWidth={false}>
        <InferenceListToolbar />
        <Box sx={{ pt: 3 }}>
          <InferenceListResults inferences={inferences} />
        </Box>
      </Container>
    </Box>
  </>
);

export default InferenceList;
