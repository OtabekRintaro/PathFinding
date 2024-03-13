import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const HeadElement = screen.getByText(/PATH FINDING ALGOS/i);
  expect(HeadElement).toBeInTheDocument();
});
