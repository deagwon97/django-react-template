import { useState } from 'react';
import PropTypes from 'prop-types';
import moment from 'moment';
import PerfectScrollbar from 'react-perfect-scrollbar';
import {
  Avatar,
  Box,
  Card,
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TablePagination,
  TableRow,
  Typography
} from '@material-ui/core';
import getInitials from 'src/utils/getInitials';

const InferenceListResults = ({ inferences, ...rest }) => {
  const [selectedInferenceIds, setSelectedInferenceIds] = useState([]);
  const [limit, setLimit] = useState(10);
  const [page, setPage] = useState(0);

  const handleSelectAll = (event) => {
    let newSelectedInferenceIds;

    if (event.target.checked) {
      newSelectedInferenceIds = inferences.map((inference) => inference.id);
    } else {
      newSelectedInferenceIds = [];
    }

    setSelectedInferenceIds(newSelectedInferenceIds);
  };

  const handleSelectOne = (event, id) => {
    const selectedIndex = selectedInferenceIds.indexOf(id);
    let newSelectedInferenceIds = [];

    if (selectedIndex === -1) {
      newSelectedInferenceIds = newSelectedInferenceIds.concat(selectedInferenceIds, id);
    } else if (selectedIndex === 0) {
      newSelectedInferenceIds = newSelectedInferenceIds.concat(
        selectedInferenceIds.slice(1)
      );
    } else if (selectedIndex === selectedInferenceIds.length - 1) {
      newSelectedInferenceIds = newSelectedInferenceIds.concat(
        selectedInferenceIds.slice(0, -1)
      );
    } else if (selectedIndex > 0) {
      newSelectedInferenceIds = newSelectedInferenceIds.concat(
        selectedInferenceIds.slice(0, selectedIndex),
        selectedInferenceIds.slice(selectedIndex + 1)
      );
    }

    setSelectedInferenceIds(newSelectedInferenceIds);
  };

  const handleLimitChange = (event) => {
    setLimit(event.target.value);
  };

  const handlePageChange = (event, newPage) => {
    setPage(newPage);
  };

  return (
    <Card {...rest}>
      <PerfectScrollbar>
        <Box sx={{ minWidth: 1050 }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell padding="checkbox">
                  <Checkbox
                    checked={selectedInferenceIds.length === inferences.length}
                    color="primary"
                    indeterminate={
                      selectedInferenceIds.length > 0 &&
                      selectedInferenceIds.length < inferences.length
                    }
                    onChange={handleSelectAll}
                  />
                </TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Email</TableCell>
                <TableCell>Location</TableCell>
                <TableCell>Phone</TableCell>
                <TableCell>Registration date</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {inferences.slice(0, limit).map((inference) => (
                <TableRow
                  hover
                  key={inference.id}
                  selected={selectedInferenceIds.indexOf(inference.id) !== -1}
                >
                  <TableCell padding="checkbox">
                    <Checkbox
                      checked={selectedInferenceIds.indexOf(inference.id) !== -1}
                      onChange={(event) => handleSelectOne(event, inference.id)}
                      value="true"
                    />
                  </TableCell>
                  <TableCell>
                    <Box
                      sx={{
                        alignItems: 'center',
                        display: 'flex'
                      }}
                    >
                      <Avatar src={inference.avatarUrl} sx={{ mr: 2 }}>
                        {getInitials(inference.name)}
                      </Avatar>
                      <Typography color="textPrimary" variant="body1">
                        {inference.name}
                      </Typography>
                    </Box>
                  </TableCell>
                  <TableCell>{inference.email}</TableCell>
                  <TableCell>
                    {`${inference.address.city}, ${inference.address.state}, ${inference.address.country}`}
                  </TableCell>
                  <TableCell>{inference.phone}</TableCell>
                  <TableCell>
                    {moment(inference.createdAt).format('DD/MM/YYYY')}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Box>
      </PerfectScrollbar>
      <TablePagination
        component="div"
        count={inferences.length}
        onPageChange={handlePageChange}
        onRowsPerPageChange={handleLimitChange}
        page={page}
        rowsPerPage={limit}
        rowsPerPageOptions={[5, 10, 25]}
      />
    </Card>
  );
};

InferenceListResults.propTypes = {
  inferences: PropTypes.array.isRequired
};

export default InferenceListResults;
