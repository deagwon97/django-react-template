import { Helmet } from 'react-helmet';
import { Box, Container } from '@material-ui/core';
import UserListResults from 'src/components/user/UserListResults';
import UserListToolbar from 'src/components/user/UserListToolbar';
import users from 'src/__mocks__/users';

const UserList = () => (
  <>
    <Helmet>
      <title>Users | Material Kit</title>
    </Helmet>
    <Box
      sx={{
        backgroundColor: 'background.default',
        minHeight: '100%',
        py: 3
      }}
    >
      <Container maxWidth={false}>
        <UserListToolbar />
        <Box sx={{ pt: 3 }}>
          <UserListResults users={users} />
        </Box>
      </Container>
    </Box>
  </>
);

export default UserList;
