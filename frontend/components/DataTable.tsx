import React from 'react';
import { useTable, Column, usePagination, useSortBy } from 'react-table';

interface DataTableProps<T extends object> {
  columns: Column<T>[];
  data: T[];
}

const DataTable = <T extends object>({ columns, data }: DataTableProps<T>) => {
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
    page,
    nextPage,
    previousPage,
    canPreviousPage,
    canNextPage,
  } = useTable({ columns, data }, useSortBy, usePagination);

  return (
    <div className="overflow-x-auto">
      <table {...getTableProps()} className="min-w-full bg-white">
        <thead>
          {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps(column.getSortByToggleProps())} className="py-2 px-4 border-b">
                  {column.render('Header')}
                  <span>
                    {column.isSorted ? (column.isSortedDesc ? ' 🔽' : ' 🔼') : ''}
                  </span>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {page.map(row => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()} className="hover:bg-gray-50">
                {row.cells.map(cell => (
                  <td {...cell.getCellProps()} className="py-2 px-4 border-b">
                    {cell.render('Cell')}
                  </td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="mt-2">
        <button onClick={() => previousPage()} disabled={!canPreviousPage} className="mr-2 px-4 py-2 bg-gray-200 rounded">
          Previous
        </button>
        <button onClick={() => nextPage()} disabled={!canNextPage} className="px-4 py-2 bg-gray-200 rounded">
          Next
        </button>
      </div>
    </div>
  );
};

export default DataTable;